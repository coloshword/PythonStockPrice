import requests
from bs4 import BeautifulSoup
import time


def main():
    with open('stock_dictionary.txt', 'r') as fh:
        for URL in fh.readlines():
            page = requests.get(URL.replace('\n', ''))
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
            print(results)

while True:
    main()
    time.sleep(60)