import urllib.request
import bs4 as bs

print("Buscando a pagina...")
url = "https://www.valor.com.br/"
pagina = urllib.request.urlopen(url)
codigo_pagina = bs.BeautifulSoup(pagina, features="html.parser")

conteudo = codigo_pagina.find('h2', attrs={'class': 'title1'})  # elemento 'h2' que tiver um atributo=={classe e tittle1}
print(conteudo.text.strip())
