import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# URL da página da web
url = "https://ultimate-mushroom.com/poisonous/27-amanita-phalloides.html"

# Enviar uma solicitação GET para a URL e obter o conteúdo da página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Obter o conteúdo HTML da página
    html = response.text

    # Parseie o HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontre a classe "full_title" e obtenha o texto dela
    full_title_element = soup.find(class_='full_title')
    name = full_title_element.get_text() if full_title_element else ''

    # Inicialize dicionários para armazenar os dados
    dados = {'Color': [], 'Shape': [], 'Surface': [], 'Type': [], 'Name': [name]}

    # Encontre a div com a classe "mprofile"
    mprofile_div = soup.find('div', class_='mprofile')

    # Encontre todos os elementos <p> dentro da div
    p_elements = mprofile_div.find_all('p')

    # Itere sobre os elementos <p>
    for p_element in p_elements:
        # Encontre o elemento <strong> dentro de <p>
        strong_element = p_element.find('strong')

        if strong_element:
            coluna = strong_element.get_text().strip(':')

            # Encontre todos os elementos <a> dentro de <p> após o <strong>
            a_elements = p_element.find_all('a')

            # Obtenha os textos dos elementos <a> e adicione-os ao dicionário apropriado
            for a_element in a_elements:
                texto = a_element.get_text()
                dados[coluna].append(texto)

    # Extrair o tipo (poisonous, edible, inedible) do URL
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    if len(path_parts) >= 2:
        tipo = path_parts[1]  # O tipo está na segunda parte do caminho

        # Adicionar o tipo à lista "Type"
        dados['Type'].append(tipo)
    
    # Para apagar todas as listas
    #for key in dados:
    #  dados[key] = []

    # Agora, você tem os dados em dicionários onde as chaves são os nomes das colunas
    # e os valores são listas de pontos correspondentes a cada coluna, incluindo "Type" e "Name".
    print("Color:", dados['Color'])
    print("Shape:", dados['Shape'])
    print("Surface:", dados['Surface'])
    print("Type:", dados['Type'])
    print("Name:", dados['Name'])
else:
    print("Erro ao fazer a solicitação HTTP.")
