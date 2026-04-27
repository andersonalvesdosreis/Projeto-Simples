import json
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('punkt_tab')
stemmer = PorterStemmer()
import torch
import torchtext
from torchtext.data.utils import get_tokenizer
import os
data = {
    "intents": [
        {"tag": "ajuda", "patterns": ["Preciso de ajuda", "ajude-me"], "responses": ["Estou aqui!"]}
    ]
}

words = []
classes = []
documents = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
words = [stemmer.stem(w.lower()) for w in words if w != '?']
words = sorted(list(set(words)))
