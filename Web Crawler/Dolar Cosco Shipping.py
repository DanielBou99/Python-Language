import urllib.request
import os

while (True):

    # Importar o html do site
    content = urllib.request.urlopen("https://coscoshipping.com.br/pt/home/").read()
    content = str(content)

    # Localizar o dolar no html
    find = '<span class="icon-box__subtitle">08/11/2018 - $ '
    posicao = int(content.index(find)) + len(find)
    dolar = content[posicao : posicao + 4]

    # Localizar a data do dolar
    find = '<span class="icon-box__subtitle">'
    posicao = int(content.index(find)) + len(find)
    data = content[posicao : posicao + 10]

    print('Data: {}'.format(data))
    print('Dolar: {}'.format(dolar))
    os.system('pause')

