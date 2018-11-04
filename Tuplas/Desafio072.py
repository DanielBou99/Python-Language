#Desafio 072

extenso = ('zero','um','dois','três','quatro','cinco','seis',
'sete','oito','nove','dez','onze','doze','treze','catorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Digite um número entre 0-20: '))

while True:
    if n >= 0 and n <=20:
        break
    else:
        n = int(input('Tente novamente. Digite um número entre 0-20: '))

print(f'Você digitou o número {extenso[n]}')
