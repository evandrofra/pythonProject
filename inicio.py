class inicio_c:
    def __init__(self):
        self.nome = 'Evandro'
        self.idade = 50

    def mostra_dados(self):
        print(self.nome)
        print(self.idade)

    def eu(self):
        print(self.__ne__)


def f1(x):
    return x + 10


from func1 import *

pessoa = inicio_c()
print(pessoa.mostra_dados())
print(inicio_c.__name__)
funcao = f1
print(funcao.__name__)
print(funcao(5))
a=10
print(soma(a, 20))
