import requests
from bs4 import BeautifulSoup

from links import LINK_1, LINK_2


def extractData(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def crawlerInfoMoney():
    soup = extractData(LINK_1)

    positiveActions, negativeActions = soup.find_all("table",{"class": "default-table"})

    return positiveActions, negativeActions

teste = crawlerInfoMoney()
print(teste)

