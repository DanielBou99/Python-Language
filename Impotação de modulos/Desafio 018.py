# Desafio 018

import math

angulo = int(input('Informe o ângulo:\n>>>'))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Cosseno={}\nSeno={}\nTangente={}'.format(cosseno, seno, tangente))
