

class Imovel(object):
    __area = 0.0
    __valorm2 = 0.0

    def __init__(self, valorm2, area):
        self.__valorm2 = valorm2
        self.__area = area

    def calcularIPTU(self):
        return self.__area * self.__valorm2

class Casa(Imovel):
    __area_construida = 0.0
    __taxa_construcao = 0.0

    def __init__(self, area_construida, taxa_construcao, valorm2, area):
        super().__init__(valorm2, area)
        self.__area_construida = area_construida
        self.__taxa_construcao = taxa_construcao

    def calcularIPTU(self):
        return (self.__area_construida * self.__taxa_construcao) + Imovel.calcularIPTU(self)
