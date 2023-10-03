import requests
from bs4 import BeautifulSoup

from links import LINK_1, LINK_2

def extractData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def crawlerInfoMoney():
    soup = extractData(LINK_1)

    table = soup.find("table", {"class": "default-table"})

    rows = table.find_all("tr")

    data = []

    for row in rows:
        # Encontrar todas as tags <a> dentro da linha
        a_tags = row.find_all("a")
        
        # Iterar sobre as tags <a> e extrair o atributo 'href'
        href_values = [a['href'] for a in a_tags]

        # Extrair o texto das células restantes
        cell_texts = [cell.text.strip() for cell in row.find_all("td")]

        # Adicionar os valores ao data
        row_data = href_values + cell_texts
        data.append(row_data)

    print(data)
    return data
def crawlerValorInvest():
    soup = extractData(LINK_2)
    
    

teste = crawlerInfoMoney()
