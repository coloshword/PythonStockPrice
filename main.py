import requests
from bs4 import BeautifulSoup

URL = 'https://ca.finance.yahoo.com/quote/fcel'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#<div class=”My(6px) Pos(r) smartphone_Mt(6px)”>
results = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
print(results.prettify())

# big dik