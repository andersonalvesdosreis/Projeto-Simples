from time import sleep
print('='*50)
login = str(input('Crie um login para acessar o programa: '))
senha = str(input('Crie uma senha para acessar o progama: '))
print('='*50)
print('='*15,'Bem vindo ao sistema simples de login','='*15)
tentativa = str(input('login: '))
senha2 = str(input('Digite a Senha: '))
print('='*50)
print('Conferindo...')
sleep(1)
print('='*50)
while tentativa != login or senha2 != senha:
    tentativa2 = str(input('Login errado tente novamente: '))
    senha3 = str(input('Senha errada tente novamente: '))
    print('Conferindo...')
    sleep(1)
    if tentativa2 == login:
        if senha3 == senha:
            break
        else:
            print(' '*30,'\033[31mSenha incorreta!\033[m')
            print('='*50)
            continue
    else:
        print(' '*30,'\033[31mLogin Errado!\033[m')
        print('='*50)
        continue
