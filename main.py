import requests
from bs4 import BeautifulSoup
import time


def main():
    with open('stock_dictionary.txt', 'r') as fh:
        for URL in fh.readlines():
            page = requests.get(URL.replace('\n', ''))
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
            header = URL[35:].replace('\n', "")
            print(header + " : $" + results)


while True:
    print('-' * 30)
    main()
    time.sleep(60)