import os
print('Bem vindo ao jogo do par ou impar!')

number = int(input('Insira um número: '))

def numero_par():
    
    
    os.system('cls')
    print('Este número é par\n')

def numero_impar():
        os.system('cls')
        print('Este número é impar\n')

def verifica_numero():

    if number%2==0:
        numero_par()
    else:
        numero_impar()
       
verifica_numero()