#Desafio 066

s = 0
k = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    k += 1
print(f'A soma dos {k} valores foi {s}!')