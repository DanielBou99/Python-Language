'''
Crie uma classe pai Quadrilatero que possui dois atributos: base e altura, e dois métodos
calcular_area() e calcular_perimetro(). Uma classe filha Quadrado, que em seu
construtor recebe 1 parâmetro que o tamanho do lado do quadrado, e atribui este valor a
base e altura da classe pai, não precisando escrever novamente os métodos.
Uma classe filha Trapezio, posui um atributo base_menor, e seu construtor recebe os parametros
base maior, base menor e altura, e deve sobreescrever o método da classe pai
calcular_area() com o cálculo ((base maior+ base menor)*h)/2.
Crie 3 objetos (1 objeto da classe Quadrilátero, 1 objeto da classe Quadrado, e 1 objeto da classe Trapezeio,
coloque-os em uma lista, e utilizando do polimorfismo calcule a soma dos perimetros e
das área de todos os objetos.
'''

class Quadrilatero(object):

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        print(f'Calcular area: {self.__base * self.__altura}')

    def calcular_perimetro(self):
        print(f'Calcular perimetro: {self.__base * 2 + self.__altura * 2}')

class Quadrado(Quadrilatero):

    ladoQuadrado = int()

    def __init__(self, ladoQuadrado):
        self.ladoQuadrado = ladoQuadrado
        Quadrilatero.__init__(self, ladoQuadrado, ladoQuadrado)

class Trapezio(Quadrilatero):

    baseMenor = int()

    def __init__(self, baseMaior, baseMenor, altura):
        self.__baseMaior = baseMaior
        self.__baseMenor = baseMenor
        self.__altura = altura
        Quadrilatero.__init__(self, baseMaior+baseMenor, altura)

    def calcular_area(self):
        print(f"calcular area {((self.__baseMaior + self.__baseMenor)* self.__altura)/2} ")
