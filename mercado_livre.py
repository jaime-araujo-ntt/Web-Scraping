import urllib.request
import bs4 as bs
def valor(p, m):
    produto = p
    url = "https://lista.mercadolivre.com.br/{}".format(produto) # ideal deixar a barra para modicicar apenas o produto
    print("Acessando site...")
    pagina = urllib.request.urlopen(url) # pegando o código da página
    codigo_pagina = bs.BeautifulSoup(pagina, features="html.parser")
    print("Pesquisando produtos...")
    itens = codigo_pagina.find_all('span', attrs={'class': 'price__fraction'}) # .FIND_ALL pega todos na página com a classe escolhida
    links = codigo_pagina.find_all('a', attrs={'class': 'item__info-title'})

    menor = m
    posicao = 0
    volta = 0
    for i in itens:
        valor = float(i.text.strip().replace('.',''))  # retirar o ponto do R$ 1.000,00 para retirar o erro do Float
        if valor <= menor:
            menor = valor
            posicao = volta
        volta = volta + 1
    print(menor, posicao)  # check de mudança de posição.
    print(links[posicao].get('href'))  # href referente ao links.

if __name__ == '__main__':
    valor()