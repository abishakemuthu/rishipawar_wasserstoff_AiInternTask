from pymongo import MongoClient
import urllib.parse

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