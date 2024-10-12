from collections import Counter
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
nlp = spacy.load('en_core_web_sm')
from sklearn.feature_extraction.text import TfidfVectorizer
stopwords = list(STOP_WORDS)
allowed_pos = ['ADJ','PROPN','VERB','NOUN']

def preprocess_text(text):
    doc =  nlp(re.sub(r'\s+', ' ', text)) # Clean spaces, tabs and newlines
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