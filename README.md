
## Text Summarization Project

![Text Sum](https://github.com/user-attachments/assets/55caa3e0-e400-477f-af4b-86d878d90e11)

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
