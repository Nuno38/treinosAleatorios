import os

class ContaBancaria:
    dados_bancarios = []
    
    def __init__(self, numero_da_conta=0,titular_da_conta='',saldo=0):
        
        self._numero_da_conta = numero_da_conta
        self._titular_da_conta = titular_da_conta.title()
        self._saldo = saldo
        self._status_da_conta = False
        
        ContaBancaria.dados_bancarios.append(self)
        
    def __str__(self):
        return f'{self._numero_da_conta} | {self._titular_da_conta} | {self._saldo}'
     
    @classmethod 
    def dados_da_conta(cls):
        os.system('cls')
        print(f'\n{'Número da conta'.ljust(5)}     | {'Titular da conta'.ljust(22)}       | {'Saldo'.ljust(5) }    | {'Status'.ljust(10)}')
        for conta in cls.dados_bancarios:
            print(f'   {conta._numero_da_conta}          | {conta._titular_da_conta.ljust(24)}     | {conta._saldo}     | {conta._status_da_conta}')
            
            
    @property
    def status(sef):
        return 'Ativo' if sef._status_da_conta else 'False'
    
    def altera_status(sef):
        sef._status_da_conta = not sef._status_da_conta
        
        

conta1 = ContaBancaria(1170530,'elias joão do nascimento', 3000)
conta2 = ContaBancaria (3526878, 'ricador luiz rosa',5000)
conta1.altera_status()
conta2.altera_status()
ContaBancaria.dados_da_conta()
