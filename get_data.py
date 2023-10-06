import requests
from bs4 import BeautifulSoup

def find_links_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a')]
            return links
        else:
            print(f"Erro ao acessar {url}. Código de status: {response.status_code}")
            return []
    except Exception as e:
        print(f"Erro ao acessar {url}: {str(e)}")
        return []

# URL de partida
start_url = 'https://ultimate-mushroom.com/mushroom-alphabet.html'

# Encontre todos os links a partir do URL de partida
links = find_links_from_url(start_url)

# Palavras-chave para procurar nos links
keywords = ['edible', 'inedible', 'poisonous']

# Use list comprehension para criar uma nova lista apenas com os links relevantes
links = [link for link in links if any(keyword in link for keyword in keywords)]

del links[:3]
del links[-3:]

# Imprima os links relevantes
for link in links:
    print(link)

