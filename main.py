import requests
from bs4 import BeautifulSoup
import time
import os

def main():
    with open('stock_holds.txt', 'r') as fh:
        for URL in fh.readlines():
            page = requests.get(URL.replace('\n', ''))
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
            header = URL[35:].replace('\n', "")
            print(header + " : $" + results)


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while True:
    print('-' * 30)
    main()
    time.sleep(30)