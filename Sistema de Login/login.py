from time import sleep
def senha_forte(senha_aleatoria):
        procurando_caracter = len(senha_aleatoria.strip())
        if procurando_caracter <= 8:
            print('\033[31mSenha Fraca!\033[m Digite mais de 8 caracteres!')
            while True:
                tentar_novamente = str(input('Senha errada tente novamente: \033[32m'))
                print(end='\033[m')
                procurando_caracter_novamente = len(tentar_novamente.strip())
                if procurando_caracter_novamente <= 8:
                     continue
                else:
                     break
        else:
            print('\033[34mSenha Forte!\033[m')
            return True
def email(email_nao_encontrado):
    if not '@gmail.com' in email_nao_encontrado:
        print('\033[31memail nao encontrado\033[m')
        while True:
                tentar_novamente =  str(input('Login errado tente novamente: \033[32m'))
                print(end='\033[m') 
                if not '@gmail.com' in tentar_novamente:
                     continue
                else:
                     break
    else:
        print('\033[34mEmail encontrado\033[m')
        return True
print('='*50)
print('='*15,'Bem vindo ao sistema simples de login','='*15)
print('='*50)
print('Crie um login para acessar o programa')
tentativa = email(str(input('login: \033[32m')))
print(end='\033[m')
print('='*50)
print('Crie uma senha para acessar o progama')
senha2 = senha_forte(str(input('Digite a Senha:  \033[32m')))
print(end='\033[m')
print('='*50)
print('Conferindo...')
sleep(1)
print('\033[32mEmail e Senha Fortes!\033[m')
print('='*50)
#while tentativa != True or senha2 != senha:
#    tentativa2 = str(input('Login errado tente novamente: '))
#    senha3 = str(input('Senha errada tente novamente: '))
#    print('Conferindo...')
#    sleep(1)
#    if tentativa2 == login:
#        if senha3 == senha:
#            break
#        else:
#            print(' '*30,'\033[31mSenha incorreta!\033[m')
#            print('='*50)
#            continue
#    else:
#        print(' '*30,'\033[31mLogin Errado!\033[m')
#        print('='*50)
#        continue
