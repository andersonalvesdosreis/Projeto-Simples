import json
import nltk
import numpy as np
from nltk.stem import RSLPStemmer # Melhor stemmer para português
from nltk.tokenize import word_tokenize
import os

# Download necessário para tokenização
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('rslp')

# Inicializa o Stemmer para Português
stemmer = RSLPStemmer()

# --- 1. DADOS EXPANDIDOS ---
data = {
    "intents": [
        {
            "tag": "saudacao",
            "patterns": ["Oi", "Olá", "Bom dia", "Boa tarde", "Tudo bem?", "Ei"],
            "responses": ["Olá! Como posso ajudar?", "Oi, tudo bem?", "Olá!"]
        },
        {
            "tag": "ajuda",
            "patterns": ["Preciso de ajuda", "ajude-me", "o que você faz?", "suporte"],
            "responses": ["Estou aqui! Posso ajudar com dúvidas simples.", "Claro, qual sua dúvida?"]
        },
        {
            "tag": "despedida",
            "patterns": ["Tchau", "Até logo", "Adeus", "Até mais"],
            "responses": ["Até logo!", "Tchau, tchau!", "Até a próxima!"]
        }
    ]
}

# --- 2. PROCESSAMENTO E TOKENIZAÇÃO ---
words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokeniza cada palavra
        w = word_tokenize(pattern.lower(), language='portuguese')
        words.extend(w)
        # Adiciona aos documentos
        documents.append((w, intent['tag']))
        # Adiciona tags às classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# --- 3. STEMMING E LIMPEZA ---
# Stemming + remove acentos e palavras irrelevantes
words = [stemmer.stem(w) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# --- 4. TRADUÇÃO PARA NÚMEROS (BAG OF WORDS) ---
print("Criando vocabulário e traduzindo para números...")

training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    
    # Cria o vetor Bag of Words (1 se a palavra existe, 0 se não)
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
        
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])

# Exemplo de saída numérica
print(f"Palavras mapeadas: {len(words)}")
print(f"Classes mapeadas: {len(classes)}")
print(f"Exemplo de Bag of Words (primeira frase): {training[0][0]}")
print(f"Exemplo de Classificação (primeira frase): {training[0][1]}")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#limpar_terminal()
