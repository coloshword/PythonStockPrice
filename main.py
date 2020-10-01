import requests
from bs4 import BeautifulSoup
import time

URL = 'https://ca.finance.yahoo.com/quote/fcel'
URL2 = 'https://ca.finance.yahoo.com/quote/aapl'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#<div class=”My(6px) Pos(r) smartphone_Mt(6px)”>
results = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.content,'html.parser')
results2 = soup2.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

print(results)
print(results2)