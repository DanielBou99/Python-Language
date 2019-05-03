'''
Programa deve perguntas quantos dipositivos existem, quais são eles,
quais estão ligados e calcular o consumo total de banda.
'''

from calculardispositivos import *

n = int(input('Quantos dispositivos?'))

total = 0
total_smartphone = 0
total_tablet = 0
total_pc = 0
lista = []

for k in range(0,n):
    ip = input('IP: >>> ')
    ligado = bool(input('Ligado? True/False: >>> '))
    aplicacao = int(input('Aplicacao (0,1 ou 2): >>> '))
    dispositivo = int(input('Dispositivo (0=Smartphone|1=Tablet|2=PC): >>> '))


    if (dispositivo == 0):
        aux = SmartPhone(ip, ligado, dispositivo)
        lista.append(aux)
    elif (dispositivo == 1):
        aux = Tablet(ip, ligado, dispositivo)
        lista.append(aux)
    elif (dispositivo == 2):
        aux = Pc(ip, ligado, dispositivo)
        lista.append(aux)

for i in lista:
    total += i.getConsumo()


print(f'Total consumo = {total}mb/s.')