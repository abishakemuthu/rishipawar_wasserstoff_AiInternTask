from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import string
#import spacy
#from spacy.lang.en.stop_words import STOP_WORDS
#from string import punctuation
#nlp = spacy.load('en_core_web_sm')
#stopwords = list(STOP_WORDS)
#allowed_pos = ['ADJ','PROPN','VERB','NOUN']

#def preprocess_text(text):
#    doc =  nlp(re.sub(r'\s+', ' ', text)) # Clean spaces, tabs and newlines
#    tokens = []
#    for token in doc:
#        if token.text in stopwords or token.text in punctuation:
#            continue
#        if token.pos_ in allowed_pos:
#            tokens.append(token.text.strip())
#    return " ".join(tokens)

def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r'<.*?>', '', text) # Remove HTML tags
    text = re.sub(r'[^\x00-\x7f]', r'', text) # Remove non-ascii characters
    text = text.lower() # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text


def extract_keywords(text):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)