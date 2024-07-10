class Restaurante:
    def __init__(self, nome, categoria):
        self.nome =''
        self.categoria =''
        self.ativo = False
    
    
samuray_lanche = Restaurante('Samuray lanche','Delivery')
boca_sushi = Restaurante('Boca', 'Sushi')


print('Nome |  Categogria  |  Status')
print(vars(boca_sushi))