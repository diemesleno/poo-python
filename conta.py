

class Conta:
    
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))