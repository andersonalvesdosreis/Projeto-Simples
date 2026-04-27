🤖 Chatbot NLP - Processamento de Linguagem Natural com NLTK
Este projeto é um motor de processamento de texto para um Chatbot inteligente. Ele utiliza técnicas de NLP (Natural Language Processing) para entender intenções do usuário, transformando frases em português em vetores numéricos que uma Inteligência Artificial pode processar.

🧠 Conceitos Aplicados
Neste projeto, apliquei os pilares fundamentais do pré-processamento de dados para IA:

Tokenização: Quebra das frases em unidades menores (palavras/tokens).

Stemming (RSLP): Técnica que reduz a palavra ao seu radical (ex: "ajudando", "ajuda" e "ajudei" viram apenas "ajud"). Isso ajuda o bot a entender variações da mesma palavra.

Bag of Words (Saco de Palavras): Conversão de texto em uma matriz binária (0 e 1), permitindo que modelos matemáticos processem a linguagem humana.

Mapeamento de Intenções (Intents): Organização de padrões de fala em categorias como saudacao, ajuda e despedida.

🛠️ Tecnologias e Bibliotecas
Python 3: Linguagem base.

NLTK (Natural Language Toolkit): A principal biblioteca de Python para trabalhar com dados de linguagem humana.

NumPy: Para manipulação de vetores e matrizes numéricas.

JSON: Para estruturar o conhecimento do bot.

📖 Como o Código Funciona?
1. O Vocabulário
O código lê um dicionário de intenções e extrai todas as palavras únicas, limpando sinais de pontuação.

2. O Processo de Stemming
Utilizei o RSLPStemmer, que é o melhor extrator de radicais focado especificamente na língua portuguesa.

Python
# Exemplo do que acontece por baixo dos panos:
# "Olá, como posso ajudar?" -> ["olá", "com", "poss", "ajud"]
3. Vetorização (Bag of Words)
Para cada frase de treino, o sistema cria uma lista de 0 e 1 comparando com o vocabulário global. Se a palavra do vocabulário existe na frase, ele marca 1, se não, 0.

🚀 Como Executar
Instale as dependências necessárias:

Bash
pip install nltk numpy
Execute o script:

Bash
python nome_do_arquivo.py
Nota: Na primeira execução, o script baixará automaticamente os pacotes punkt e rslp do NLTK.

📈 Próximos Passos
Este código é a base (o cérebro) para:

[ ] Treinar uma Rede Neural com os dados gerados.

[ ] Criar uma interface de chat em tempo real.

[ ] Adicionar mais intenções e respostas dinâmicas.

Projetado com foco em entender como a IA "lê" o que escrevemos. 🚀