#Desafio 053

user = str(input('Digite a palavra: '))

user = user.upper().strip().split()
user = ''.join(user)

c = 0
j = len(user) - 1

for i in range (0,len(user)):
    # print('User[i]: {} == User [j]: {}'.format(user[i],user[j]))
    if user[i] == user[j]:
        c += 1
    j -= 1
if c == len(user):
    print('É um palíndromo.')
else:
    print('NÃO é um palíndromo.')
