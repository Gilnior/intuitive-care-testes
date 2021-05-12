import requests
from bs4 import BeautifulSoup

source = requests.get('http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar').text
soup = BeautifulSoup(source, 'lxml')

print(soup)


