'''
3. Aplicando o Paradigma Orientado a Objeto
a. Crie uma classe com um atributo nums, um método maior() que irá retornar
o maior número, um método menor() que irá retornar o menor número. Entre com
uma sequencia numérica de inteiros em uma linha, instancie um objeto, e
exiba na tela o retorno dos métodos maior e menor deste objeto.

'''

from orientado_a_objetos_a_orientacao import *

numeros = [1,2,3,4,5,6,7,8,9]
maior = Maior(numeros)
menor = Menor(numeros)
funcoes = [maior,menor]
for i in funcoes:
    i.exibir()
