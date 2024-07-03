
#idade = int (input("Digite a idade da pesso: "))


#if idade >18:
    #print("Maior de idade")
#else:
    #print("Menor de idade")
    
   ####
   
####------
# A = int(input("Insira primeira nota: "))
####B = int (input("Insira segunda nota: "))

####mediaFinal= (A+B)/2

####if mediaFinal >= 7.0:
    
   #### print("Aprovado %.1f" % mediaFinal)
    
####else:
   #### print("Reprovado %.1f "% mediaFinal)

import os

restaurantes = [{'Nome':'Boca Sushi','Categoria':'Comida Japonesa','Ativo':False},
                {'Nome': 'Snoop dog', 'Categoria': 'HOTDOG','Ativo':True}]


def exibir_nome_do_programa():
    
   print('\n𝕊𝕒𝕓𝕠𝕣𝕖𝕤 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 \n')
   
   
def retorna_ao_menu():
    input('\n Digite uma tecla para retorna ao menu: ')
    os.system('cls')
    ordem_apresentacao()


def exibir_subtitulo(texto):
    os.system('cls')
    linha ='*'* (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()   
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restarante')
    print('4. Sair')


def finalizar_app():
    ## os.system('clear') /mac book
    exibir_subtitulo('\n Finalizando o app. \n')


def verificacao_opcao_escolhida():
    
    print ('opção invalida! \n')
    os.system('cls')
    
    print('Digite um dos números das opçãos apresentadas!\n')
    retorna_ao_menu()


def cadastrar_novo_restaurante():
     
    exibir_subtitulo('Novo cadastro.\n')
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria =input(F'Digite a categoria do restaurante,{nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome':nome_do_restaurante, 'Categoria':categoria, 'Ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante}, foi cadastrado com sucesso. ')
    
    retorna_ao_menu()
    

def listar_restaurantes():
    
    exibir_subtitulo('Lista dos restaurantes\n')
    
    print(f'{'Nome do restautante'.ljust(20)} | {'Categoria do restaurantes'.ljust(20)} | {'Status'} ')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = restaurante 
              
        print(f' - {nome_do_restaurante.ljust(18)}| {categoria.ljust(18)}        | {ativo['Ativo']}\n')
   
    retorna_ao_menu()     
  
  
  
def alternar_status_do_restaurante():
    exibir_subtitulo('Aternando status do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseta alterar o status: ')
    restaurante_encontrado =False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['Nome']:
          restaurante_encontrado = True
          restaurante['Ativo'] = not restaurante['Ativo']
          mensagem =f'O restaurante {nome_do_restaurante}, foi ativado com sucesso.' if restaurante['Ativo'] else f'O restaurante {nome_do_restaurante}, foi desativado com suceso.'
          print(mensagem)
          
    if not restaurante_encontrado:
         print('O restaurante não foi encontrado.') 
    retorna_ao_menu()
    
    
    
    
def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            os.system('cls')
            cadastrar_novo_restaurante()
            
        elif opcao_escolhida == 2:
            listar_restaurantes()
            
        elif opcao_escolhida == 3:
            alternar_status_do_restaurante()
            
        elif opcao_escolhida == 4:
            exibir_subtitulo('\n Saindo do sistema. \n')
            os.system('break')
        else:
            verificacao_opcao_escolhida()
    except:
        verificacao_opcao_escolhida()
        
        
def ordem_apresentacao():   
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()         
    
ordem_apresentacao()