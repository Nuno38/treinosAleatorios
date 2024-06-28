
print('\n Welcome the System\n')

import os


usuario = input('Informe o nome do seu usuário: ')
senha = int(input('Digite a senha: '))
os.system('cls')

                    
def verifica():
    
    user = input('Informe o nome do seu usuário: ')
    password = int(input('Digite a senha: '))

    if usuario == user and senha == password:
     os.system('cls')
     print('\n Acesso correto \n')
     
    elif usuario != user and senha !=password:
        os.system('cls')  
        print('\nDados incorretos\n')                  
    else:
     os.system('cls')
     print('\n Senha incorreta \n')
             
verifica()