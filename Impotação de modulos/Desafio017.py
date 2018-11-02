# Desafio 017

import math

oposto = int(input('Cateto oposto:\n>>>'))
adjacente = int(input('cateto adjacente:\n>>>'))
hipotenusa = math.hypot(oposto,adjacente)

print('Hipotenusa = {}'.format(hipotenusa))
