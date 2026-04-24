from time import sleep
import hashlib
import os
#Funções para verificação de senha e email:
def senha_forte(senha_aleatoria):
        procurando_caracter = len(senha_aleatoria.strip())
        if procurando_caracter <= 8:
            print('\033[31mSenha Fraca!\033[m Digite mais de 8 caracteres!')
            while True:
                tentar_novamente = str(input('Senha errada tente novamente: \033[35m'))
                print(end='\033[m')
                procurando_caracter_novamente = len(tentar_novamente.strip())
                if procurando_caracter_novamente <= 8:
                     continue
                else:
                     return senha_aleatoria
                     break
        else:
            print('\033[32mSenha Forte!\033[m')
            return senha_aleatoria
def email(email_nao_encontrado):
    if not '@gmail.com' in email_nao_encontrado:
        print('\033[31memail nao encontrado\033[m')
        while True:
                tentar_novamente =  str(input('Login errado tente novamente: \033[35m'))
                print(end='\033[m') 
                if not '@gmail.com' in tentar_novamente:
                     continue
                else:
                     email_nao_encontrado = tentar_novamente
                     break
    else:
        print('\033[32mEmail encontrado\033[m')
        return email_nao_encontrado
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#Painel do sistema:
print('='*50)
print('='*10,'Bem vindo ao sistema simples de login','=')
print('='*50)
print('Crie um login para acessar o programa (use o seu email)')
tentativa = email(str(input('login: \033[32m')))
print(end='\033[m')
print('='*50)
pergunta1 = str(input('Qual seu nome? \033[32m')).strip()
print(end='\033[m')
print('='*50)
print('Crie uma senha para acessar o progama (deve ter pelo menos 8 caracteres)')
senha = senha_forte(str(input('Digite a Senha:  \033[32m')))
print(end='\033[m')
print('='*50)
print('Conferindo...')
sleep(1)
print('\033[32mEmail e Senha Fortes!\033[m')
limpar_terminal()
print('='*50)
entrar = str(input(('Login: \033[32m')))
print(end='\033[m')
senha_entrar = str(input('Senha: \033[32m'))
print(end='\033[m')
#Verificação para ver se o usuario existe ou não:
while True:
     if entrar != tentativa or senha_entrar != senha:
          print('\033[31mUsuario ou Senha Errados!\033[m Tente Novamente em Aqui em Baixo!')
          print('='*50)
          entrar = str(input(('Login: \033[32m')))
          print(end='\033[m')
          senha_entrar = str(input('Senha: \033[32m'))
          print(end='\033[m')
     else:
          print('='*50)
          sleep(0.2)
          limpar_terminal()
          break
#Criptografar senhas:
hash_objeto = hashlib.sha256(senha.encode())
senha_final = hash_objeto.hexdigest()
#Mostrar os dados do cadastro no terminal:
print('='*50)
print(f'Olá {pergunta1}, você concluiu o cadastro com sucesso!')
print(f'login: {entrar}')
print(f'Senha: {senha}')
print(f'Senha Criptografada: {senha_final}')
#Explicação do uso das Senhas Criptografadas:
print('\033[36mPorque se usa Senha Criptografada?\033[m \033[31mA criptografia impede que senhas não criptografadas sejam acessadas por quaisquer usuários e administradores de sistemas.\033[m')
print('='*50)