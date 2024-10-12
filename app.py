import os
import tempfile
import time
import streamlit as st
from parallel_processing import process_document
from pdf_processor import extract_text_from_pdf
from preprocess import preprocess_text, extract_keywords
from model import textsum_model
from params import summarize
from database import store_summary_to_db
from performance import measure_total_performance

st.title('PDF Summarizer📖')
st.subheader('Looking to save time by summarizing large documents? Simply upload the PDF you wish to summarize and let us handle the rest. ⏳')

files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if files:
    model, tokenizer = textsum_model()

    for file in files:
        file_name = file.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file: # Temporary file to store the uploaded PDF.
            tmp_file.write(file.read())
            temp_file_path = tmp_file.name  # Temporary file path.

        st.write(f"**File Name:** {file_name}")
        st.write(f"**File Size:** {round(os.path.getsize(temp_file_path)/1048576, 2)} MB")

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
            st.write(f"**Total Processing Time:** {round(total_time,2)} seconds")
            st.write("### Thank You ")

        except Exception as e:
            st.error(f"Error processing {file_name}: {str(e)}")

        os.remove(temp_file_path) # Delete the temporary file after processing.
