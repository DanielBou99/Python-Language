'''
3. Aplicando o Paradigma Orientado a Objeto
a. Crie uma classe com um atributo nums, um método maior() que irá retornar
o maior número, um método menor() que irá retornar o menor número. Entre com
uma sequencia numérica de inteiros em uma linha, instancie um objeto, e
exiba na tela o retorno dos métodos maior e menor deste objeto.
'''

class Exercicio(object):
    
    __nums = list()

    def __init__(self, nums):
        self.__nums = nums
    def exibir(self):
        print("BASIC")

class Maior(Exercicio):

    def __init__(self, nums):
        self.__nums = nums

    def exibir(self):
        print(f'Maior: {max(self.__nums)}')

class Menor(Exercicio):

    def __init__(self, nums):
        self.__nums = nums

    def exibir(self):
        print(f'Menor: {min(self.__nums)}')
