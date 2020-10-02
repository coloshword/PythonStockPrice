import requests
from bs4 import BeautifulSoup
import time
import os
stock_dict = {}


def create_dict():
    global stock_dict
    with open('stock_holds.txt', 'r') as fh:
        for line in fh.readlines():
            line = line.replace('\n', '')
            url_price = line.split(':')
            stock_dict[url_price[0] + ":" + url_price[1]] = float(url_price[2])


def main():
    create_dict()
    for key in stock_dict:
        page = requests.get(key.replace(' ', ''))
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        header = key[35:].replace('\n', "")
        print(header + " : $" + results)


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while True:
    print('-' * 30)
    main()
    time.sleep(30)