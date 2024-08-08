class Pessoa:
    pessoas =[]
     
    def __init__(self, nome, idade , profissao):
      self._nome = nome.title()
      self._idade = idade
      self._profissao = profissao.title()
      
      Pessoa.pessoas.append(self)
      
    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'
    
    
    @classmethod
    def lista_de_pessoas(cls):
        print(f'{'Nome'.ljust(25)} | {'Idade'.ljust(25)} | {'Profissao'.ljust(25)}')
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome.ljust(25)} | {pessoa._idade.ljust(25)} | {pessoa._profissao.ljust(25)}')
            
individo = Pessoa('elias joão do nascimento', '36', 'desenvolvedor')
Pessoa.lista_de_pessoas()