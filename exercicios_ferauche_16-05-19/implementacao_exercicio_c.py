from exercicio_c import *

quadrilatero = Quadrilatero(5,5)
quadrado = Quadrado(10)
trapezio = Trapezio(2,5,1)

lista = [ quadrilatero, quadrado, trapezio]

for i in lista:
    i.calcular_area()
    i.calcular_perimetro()