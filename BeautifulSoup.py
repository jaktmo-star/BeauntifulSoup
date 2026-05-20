#autor: Elcio Mello
#projeto: Raspagem de dados

# Importar bibliotecas
# pip install beautifulsoup4 requests 
from bs4 import BeautifulSoup

#Abrir o arquivo HTML
with open ('index.html','r',encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Leitura do HTML
site = BeautifulSoup(conteudo, 'html.parser')

# Buscar todos os cads da página
produtos = site.find_all('div', class_='card')

#Loop para percorrer os produtos
for produto in produtos:
    nome = produto.find('div',class_='nome').text.strip()#captura somente uma informação
    preco = produto.find('div', class_='preco').text.strip()
    print('------------------------------')
    print(f'O nome do produto é: {nome}')
    print(f'O preço do produto é: {preco}')