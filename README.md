
## Text Summarization

![cover](https://github.com/user-attachments/assets/5cfae579-f2ba-4801-b31d-7cc009365b5d)

## Objective

Developed an automated text summarization pipeline to extract concise summaries and key insights from domain-specific PDFs. Implemented parallel processing and efficient error handling to optimize performance for large document sets. Integrated MongoDB for structured storage of metadata, summaries and keywords.

## Principles

- Our application has to process single or multiple pdf which will be uploaded by user.

- It should display the metadata to the user interface.

- It should process the text present in the pdf and give concise summary according to the length of pdf text.

- It should extract the keywords from the document given to it.

- It should calculate the processing time and display it to the user for measuring performance.

- It should save the metadata, extracted summary and keywords to the mongodb Atlas which can be extracted later for analysis purpose.

## Model

- The PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive Summarization) is a machine learning model designed to automatically generate concise summaries of long documents developed by google.

- Pegasus is based on transformer architecture which will extract the important text from the given documents and convert them into concise summary that will be simple and more readable.

- Pegasus achieves SOTA summarization performance on all 12 downstream tasks, as measured by ROUGE and human evaluation.

## Performance

![Performance](https://github.com/user-attachments/assets/36d6de3e-47c9-4add-9606-cf6aa9e66e23)

## Setup Instructions

- Step 1: Install the packages mentioned in the requirement.txt (optional but recommended: create a virtual environment).
- Step 2: In Bash, type the code "streamlit run app.py" to run the user interface.
- step 3: Insert the pdf you like to summarize and the application will handle the rest.

## Procedure

- I have used streamlit for user interface, the file uploader function will get the pdf from user and give it to the pdf_processor.
- I have used pdfplumber to extract text from pdf and store it to varibale.
- I have displayed the file name and file size in the user interface.
- The text stored in the variable is cleaned properly like removel of urls, HTML tags, non-ascii characters, extra spaces, punctuation and convert all text into smaller case, giving it to the pegasus model.
- The given text is processed by the model and returned as concise summary that will be displayed to user.
- I have used Tf-idf vectorizer to extract important keywords from the processed text and give it to user.
- I have used time library to calculate the execution time of all the process and display it to the user.
- Parallely, The metadata of the pdf like id, file name, file path and file size. And the processed summary and extracted keywords will be automatically saved in Mongodb Atlas (Cloud), because I have established a connection and created a function to fetch the metadata and pass it to cloud.
- I have created a logger with the help of loguru to ensure the pipeline should not break if in case of any error. It is just a function that will fetch the error and pass it to the user interface.
- I have used Process Pool Executor from concurrent library that will help the application to process multiple files parallely to ensure speed and consistancy.
- In Params section, I have given the summary length as 2.5% of minimum length and 10% of maximum length. So, Model will give the summary according to the length of text in the given pdf. 

## Snapshot

![Text Sum](https://github.com/user-attachments/assets/55caa3e0-e400-477f-af4b-86d878d90e11)
