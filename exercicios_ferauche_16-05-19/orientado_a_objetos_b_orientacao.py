'''
Paradigma Orientado a Objeto
b. Entre com uma sequencia de no mínimo 5 números reais, calcule a média
ponderada, utilizando 0.3 para os dois primeiros valores e para os dois
últimos valores, e a 0.1 para os valores intermediários, exiba o resultado. 
'''

class Pai(object):
    __nums = list()

    def __init__(self, nums):
        self.__nums = nums

    def exibir(self):

        resultado = 0
        aux = 1

        for i in range(0, len(self.__nums)):
            if i == 0 or i == 1:
                aux = self.__nums[i] * 0.3
            elif i == len(self.__nums)-1 or i == len(self.__nums)-2:
                aux = self.__nums[i] * 0.3
            else:
                aux = self.__nums[i] * 0.1
            resultado += aux
        print(resultado)
