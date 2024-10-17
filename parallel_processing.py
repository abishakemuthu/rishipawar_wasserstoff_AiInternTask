import os
from concurrent.futures import ProcessPoolExecutor
from pdf_processor import extract_text_from_pdf
from preprocess import preprocess_text, extract_keywords
from model import textsum_model
from params import summarize
from database import store_summary_to_db
from logger import log_error

def process_document(file_path):
    try:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        text = extract_text_from_pdf(file_path)

        processed_text = preprocess_text(text)

        model, tokenizer = textsum_model()
        summary = summarize(processed_text, model, tokenizer)

        keywords = extract_keywords(processed_text)

        store_summary_to_db(file_name, file_path, file_size, summary, keywords)
        
    except Exception as e:
        log_error(f"Error processing {file_path}: {str(e)}")

def process_multiple_documents(file_paths):
    with ProcessPoolExecutor() as executor:
        executor.map(process_document, file_paths)

