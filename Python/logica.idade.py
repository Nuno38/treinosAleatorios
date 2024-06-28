

idade =int(input('Digite sua idade: ')) 
    
def verifica_idade():
    
    if idade <= 12:
        print ('Criança')
    elif idade <=18:
        print ('Adolescente')
    else:
        print('Maior de idade')
   
        

verifica_idade()