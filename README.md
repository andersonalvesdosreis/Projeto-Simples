🚀 Meus Primeiros Projetos em Python: Do Básico à IA
Bem-vindo ao repositório dos meus primeiros passos na programação com Python! Aqui você encontrará meus projetos iniciais, onde explorei desde a lógica básica de programação e segurança até o processamento de linguagem natural (NLP) para Inteligência Artificial.

Este repositório contém dois projetos principais:

🔐 Projeto 1: Sistema de Login com Criptografia SHA-256
Um sistema de fluxo de cadastro e login via terminal, com foco em validação de dados e segurança da informação.

📋 Funcionalidades
Validação de E-mail e Senha: Garante que o usuário use um e-mail válido (ex: @gmail.com) e uma senha com pelo menos 8 caracteres.

Sistema de Tentativas: Loop de repetição (while) que exige a credencial correta para liberar o acesso.

Segurança (Hashing): Utiliza a biblioteca hashlib para converter a senha do usuário em um hash SHA-256, simulando como bancos de dados reais protegem informações sensíveis.

Interface Dinâmica: Uso de cores ANSI no terminal e limpeza automática de tela (usando a biblioteca os) para uma melhor experiência.

🤖 Projeto 2: Motor de Processamento NLP para Chatbot
Um script focado em preparar a linguagem humana para ser compreendida por uma Inteligência Artificial, utilizando técnicas de Processamento de Linguagem Natural (NLP).

🧠 Conceitos Aplicados
Tokenização: Separação de frases em palavras individuais usando a biblioteca NLTK.

Stemming (RSLP): Redução de palavras ao seu radical (ex: "ajudando" vira "ajud") com foco específico na língua portuguesa.

Bag of Words: Conversão do texto processado em matrizes numéricas (0 e 1), permitindo que a IA faça cálculos e entenda a intenção do usuário.

Mapeamento de Intenções (JSON/Dict): Organização de padrões de conversas em categorias (saudação, ajuda, despedida).

🛠️ Tecnologias e Bibliotecas Utilizadas
Python 3

NLTK (Natural Language Toolkit): Para processamento de texto.

NumPy: Para manipulação de vetores numéricos.

Hashlib: Para criptografia de dados.

OS e Time: Para manipulação do terminal e controle de fluxo.

🚀 Como executar os projetos
Certifique-se de ter o Python instalado em sua máquina.

Clone este repositório:

Bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até a pasta do projeto.

Instale as dependências (necessário para o Projeto 2):

Bash
pip install nltk numpy
Execute o arquivo desejado:

Bash
# Para rodar o sistema de login:
python sistema_login.py

# Para rodar o motor do chatbot:
python motor_chatbot.py
(Nota: Lembre-se de alterar os nomes dos arquivos .py no comando acima para os nomes reais que você salvou na sua máquina).

🧠 O que aprendi com este repositório
Este repositório marca minha evolução inicial. Aprendi a manipular strings, criar loops condicionais, proteger dados com criptografia e dar os primeiros passos no fascinante mundo da Inteligência Artificial, ensinando o computador a ler e "entender" o português.

⭐ Desenvolvido com dedicação durante meus estudos de Python.