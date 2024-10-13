
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
