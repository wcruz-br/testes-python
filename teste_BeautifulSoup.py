import requests
from bs4 import BeautifulSoup

# Fazendo a requisição para a página de notícias
url = 'https://vadebike.org'
response = requests.get(url)
html = response.text

# Criando o objeto Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Buscando todos os elementos que contêm os títulos das notícias
titulos = soup.find_all('h3', class_='article-title')

# Extraindo e imprimindo os títulos
for titulo in titulos:
    print(titulo.text.strip())

print('------------------------------------------')

# Buscando todos os elementos 'a', que representam links
links = soup.find_all('a')

# Extraindo e imprimindo os atributos 'href' de cada link
for link in links:
    href = link.get('href')
    if href:
        print(href)