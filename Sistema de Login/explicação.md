🚀 Sistema de Login Simples com Criptografia SHA-256
Este é o meu primeiro projeto desenvolvido em Python! O objetivo foi criar um sistema de fluxo de cadastro e login via terminal, focando na validação de entradas do usuário e na introdução à segurança da informação através de hashing de senhas.

📋 Funcionalidades
O sistema simula um ambiente real de autenticação, seguindo estas etapas:

Cadastro de Usuário:

Validação de e-mail (exige domínio @gmail.com).

Validação de senha forte (mínimo de 8 caracteres).

Sistema de Login:

Verificação de credenciais em tempo real.

Loop de tentativa caso o usuário ou senha estejam incorretos.

Segurança:

Criptografia da senha utilizando o algoritmo SHA-256 da biblioteca hashlib.

Interface de Usuário (Terminal):

Uso de cores ANSI para feedbacks (Verde para sucesso, Vermelho para erro).

Limpeza automática do console para melhor navegação.

🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal.

Biblioteca hashlib: Para a geração do hash de segurança das senhas.

Biblioteca os: Para manipulação do terminal (comando de limpar tela).

Biblioteca time (sleep): Para criar pausas dramáticas e melhorar a experiência do usuário.

📖 Como Funciona o Código?
1. Validações (Funções)
O código utiliza funções para garantir que os dados inseridos sejam válidos. Por exemplo, a função senha_forte utiliza um laço while True que só permite o prosseguimento se a senha tiver o comprimento adequado.

2. Criptografia SHA-256
A parte mais importante para a segurança é este trecho:

Python
hash_objeto = hashlib.sha256(senha.encode())
senha_final = hash_objeto.hexdigest()
Aqui, a senha em texto plano é convertida em uma sequência hexadecimal única. Por que isso é importante? Porque mesmo que um banco de dados seja invadido, o invasor verá apenas o código (hash) e não a senha real do usuário.

3. Experiência no Terminal
Para tornar o projeto mais amigável, utilizei códigos de cores:

\033[31m: Vermelho (Alertas)

\033[32m: Verde (Sucesso)

\033[35m / \033[36m: Cores de destaque e entrada.

🚀 Como executar o projeto
Certifique-se de ter o Python instalado.

Clone este repositório:

Bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até a pasta e execute:

Bash
python nome_do_arquivo.py
🧠 O que aprendi neste projeto
Manipulação de Strings e validação de dados.

Estruturas de repetição (while) e condicionais (if/else).

Conceitos básicos de segurança e Hashing.

Organização de código em funções para reutilização.

⭐ Este é apenas o começo da minha jornada como desenvolvedor!