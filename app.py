import os
import tempfile
import time
import streamlit as st
from pymongo import MongoClient
import urllib.parse
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from loguru import logger
import pdfplumber
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
nlp = spacy.load('en_core_web_sm')
from string import punctuation

logger.add("errors.log", level="ERROR")

username = urllib.parse.quote_plus("Abishake")
password = urllib.parse.quote_plus("Abi4@mongodb")

def connect_to_mongo():
    client = MongoClient(f"mongodb+srv://Abishake:{password}@task.rtek8.mongodb.net/?retryWrites=true&w=majority&appName=task")
    db = client["wasserstoff"]
    collection = db["task"]
    return collection

def store_summary_to_db(file_name, file_path, file_size, summary, keywords):
    collection = connect_to_mongo()
    document = {
        "file_name": file_name,
        "file_path": file_path,
        "file_size": file_size,
        "summary": summary,
        "keywords": keywords
    }
    collection.insert_one(document)

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text()])  # Avoid NoneType
    return text

def preprocess_text(text):
    stopwords = list(spacy.lang.en.stop_words.STOP_WORDS)
    allowed_pos = ['ADJ', 'PROPN', 'VERB', 'NOUN']
    doc = nlp(re.sub(r'\s+', ' ', text))  # Clean spaces, tabs and newlines
    tokens = []
    for token in doc:
        if token.text in stopwords or token.text in punctuation:
            continue
        if token.pos_ in allowed_pos:
            tokens.append(token.text.strip())
    return " ".join(tokens)

def extract_keywords(text):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)

def summarize(text, model, tokenizer, length_multiplier=0.1):
    tokens = len(tokenizer.tokenize(text))
    max_length = int(tokens * length_multiplier)  # Adjust summary length based on document size
    inputs = tokenizer(text, truncation=True, padding='longest', return_tensors="pt")
    summary_ids = model.generate(inputs['input_ids'], min_length=round(max_length * 0.025), max_length=round(max_length * 0.1), num_beams=5, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def textsum_model():
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
    return model, tokenizer

def measure_total_performance(func, *args):
    start_time = time.time()
    result = func(*args)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

st.title('PDF Summarizer📖')
st.subheader('Looking to save time by summarizing large documents? Simply upload the PDF you wish to summarize and let us handle the rest. ⏳')

files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

model, tokenizer = textsum_model()

if files:
    for file in files:
        file_name = file.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.read())
            temp_file_path = tmp_file.name  # Temporary file path.

        st.write(f"**File Name:** {file_name}")
        st.write(f"**File Size:** {round(os.path.getsize(temp_file_path) / 1048576, 2)} MB")

        try:
            def process_document_flow(file_name, temp_file_path):
                text = extract_text_from_pdf(temp_file_path)
                processed_text = preprocess_text(text)
                summary = summarize(processed_text, model, tokenizer)
                keywords = extract_keywords(processed_text)
                store_summary_to_db(file_name, temp_file_path, os.path.getsize(temp_file_path), summary, keywords)
                return summary, keywords

            (summary, keywords), total_time = measure_total_performance(process_document_flow, file_name, temp_file_path)

            st.write("### Summary:")
            st.write(summary)
            st.write("### Keywords:")
            st.write(", ".join(keywords))
            st.write(f"**Total Processing Time:** {round(total_time, 2)} seconds")
            st.write("### Thank You ")

        except Exception as e:
            logger.error(f"Error processing {file_name}: {str(e)}")
            st.error(f"Error processing {file_name}: {str(e)}")

        os.remove(temp_file_path)  # Delete the temporary file after processing.
