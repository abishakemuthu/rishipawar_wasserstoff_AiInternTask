import os
from parallel_processing import process_multiple_documents

def get_pdf_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

def main(folder_path):
    pdf_files = get_pdf_files(folder_path)
    process_multiple_documents(pdf_files)

if __name__ == "__main__":
    folder_path = "path_to_your_folder"
    main(folder_path)