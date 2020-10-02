def add_a_stock():
    urls = []
    prices = []
    base_url = 'https://ca.finance.yahoo.com/quote/'
    company = input("Enter the stock symbol: ")
    while company != "":
        price = input("Enter the price you want to sell at: ")
        url = base_url + company
        urls.append(url)
        prices.append(price)
        company = input("Enter the stock symbol: ")
    for i in range(len(urls)):
        save_data(urls[i], prices[i])


def save_data(stock, price):
    with open("stock_holds.txt", 'a') as file_body:
        lines = stock + " : " + price + '\n'
        file_body.write(lines)

add_a_stock()