import os

number = [10]
nomes =[4]
ano =[2]

def mensagem_texto(texto):
    os.system('cls')
    print(texto)
    print('')

def dados_inseridos():
    
        mensagem_texto('Welcome the System!')
        numeros= int(input('Escreva um Numero: '))
        number.append(numeros)
           
    for numero in number:
       print(f'{numero}')
           
dados_inseridos()          