import os
from Modelos.restaurante import Restaurante

restaurante_samuray = Restaurante('Smuray lanches', 'lanches')
restaurante_deck = Restaurante('Pizza Deck', 'Pizarria')
restaurante_xburguinho = Restaurante('X-Burguinho','lanches')

restaurante_xburguinho.alternar_status()
restaurante_xburguinho.avaliacao_do_cliente('Elias',10)
restaurante_xburguinho.avaliacao_do_cliente('Elias',5)
restaurante_xburguinho.avaliacao_do_cliente('Elias',4)
restaurante_xburguinho.avaliacao_do_cliente('Elias',10)
                                        
                                        
def main ():
    os.system('cls\n')
    
    Restaurante.lista_restaurantes()
    
   

if __name__ == '__main__':
    main()