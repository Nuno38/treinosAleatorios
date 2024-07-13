import os

class Carro:
    carros = []
    
    def __init__(self,nome,marca,ano,modelo):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
    
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.nome}| {self.marca} | {self.ano}| {self.modelo}'
    
    def lista_de_carros():
        for carro in Carro.carros:
            print(f'{carro.nome}| {carro.marca}| {carro.ano}| {carro.modelo}')

gol = Carro('Gol','Volkswagem','2013','Gol')            
chevrolet = Carro('Celta','Chevrolet','2024','Celta')            
            
 
Carro.lista_de_carros()           