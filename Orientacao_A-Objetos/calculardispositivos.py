'''
Programa deve perguntas quantos dipositivos existem, quais são eles,
quais estão ligados e calcular o consumo total de banda.
'''


class Dispositivo(object):
    __ip = str()
    __ligado = False
    __aplicacao = int()

    def __init__(self, ip, ligado, aplicacao):
        self.__ip = ip
        self.__ligado = ligado
        self.__aplicacao = aplicacao

    def getConsumo(self):
        pass

class SmartPhone(Dispositivo):

    __ip = str()
    __ligado = False
    __aplicacao = int()

    def __init__(self, ip, ligado, aplicacao):
        super().__init__(ip, ligado, aplicacao)
        self.__ip = ip
        self.__ligado = ligado
        self.__aplicacao = aplicacao

    def getConsumo(self):
        if self.__ligado == True:
            if self.__aplicacao == 0:
                return 300
            elif self.__aplicacao == 1:
                return 1
            elif self.__aplicacao == 2:
                return 150

class Tablet(Dispositivo):

    __ip = str()
    __ligado = False
    __aplicacao = int()

    def __init__(self, ip, ligado, aplicacao):
        super().__init__(ip, ligado, aplicacao)
        self.__ip = ip
        self.__ligado = ligado
        self.__aplicacao = aplicacao

    def getConsumo(self):
        if self.__ligado == True:
            if self.__aplicacao == 0:
                return 400
            elif self.__aplicacao == 1:
                return 10
            elif self.__aplicacao == 2:
                return 300

class Pc(Dispositivo):

    __ip = str()
    __ligado = False
    __aplicacao = int()

    def __init__(self, ip, ligado, aplicacao):
        super().__init__(ip, ligado, aplicacao)
        self.__ip = ip
        self.__ligado = ligado
        self.__aplicacao = aplicacao

    def getConsumo(self):
        if self.__ligado == True:
            if self.__aplicacao == 0:
                return 400
            elif self.__aplicacao == 1:
                return 10
            elif self.__aplicacao == 2:
                return 350
