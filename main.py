import requests
from bs4 import BeautifulSoup
import time
import os
stock_dict = {}
buy_dict = {}


def create_dict(text_file):
    global stock_dict
    global buy_dict
    if text_file == "stock_holds.txt":
        stock_dict = {}
    elif text_file == "stock_buys.txt":
        buy_dict = {}
    with open(text_file, 'r') as fh:
        for line in fh.readlines():
            line = line.replace('\n', '')
            url_price = line.split(':')
            if text_file == "stock_holds.txt":
                stock_dict[url_price[0] + ":" + url_price[1]] = float(url_price[2])
            else:
                buy_dict[url_price[0] + ":" + url_price[1]] = float(url_price[2])


def check_holds():
    create_dict('stock_holds.txt')
    for key in stock_dict:
        page = requests.get(key.replace(' ', ''))
        soup = BeautifulSoup(page.content, 'html.parser')
        price_now = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        check_value_sell(key, float(price_now))
        header = key[35:].replace(' ', "")
        print(header + " : $" + price_now)


def check_buys():
    create_dict('stock_buys.txt')
    for key in buy_dict:
        page = requests.get(key.replace(' ', ''))
        soup = BeautifulSoup(page.content, 'html.parser')
        price_now = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
        check_value_buy(key, float(price_now))
        header = key[35:].replace(' ', "")
        print(header + " : $" + price_now)


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def check_value_sell(company, current_price):
    value_to_check = stock_dict[company]
    if current_price >= value_to_check:
        message = f"Sell {company[35:]}, it is {current_price - value_to_check} above your sell price"
        notify('SELL', message)


def check_value_buy(company, current_price):
    value_to_check = buy_dict[company]
    if current_price <= value_to_check:
        message = f" Buy {company[35:]}, it is {current_price - value_to_check} below your buy price"
        notify('SELL', message)


while True:
    try:
        print('-' * 15, "WATCHLIST", '-' * 15)
        check_buys()
        print('-' * 15, "CURRENT STOCKS IN POSSESSION", '-' * 15)
        check_holds()
        time.sleep(30)
    except AttributeError:
        notify('CODE BROKE', 'RESTART')
        break