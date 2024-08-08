from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def lista_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Status'.ljust(25)} |{'Avaliação'.ljust(25)}')
        
        for restaurante in cls.restaurantes:
          print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}|{restaurante.calculo_da_avaliacao}') 
    
    @property
    def ativo(self):
        return'Ativo' if self._ativo else 'False'
    
    def alternar_status(self):
        self._ativo = not self._ativo
    
    def avaliacao_do_cliente(self,cliente,nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def calculo_da_avaliacao(self):
        
        if not self._avaliacao:
           return 0
     
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
        
samuray_lanche = Restaurante('samuray lanche','Delivery')
boca_sushi = Restaurante('boca', 'Comida japonesa')


Restaurante.lista_restaurantes()