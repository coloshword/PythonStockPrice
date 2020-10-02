def add_a_stock():
    urls = []
    prices = []
    base_url = 'https://ca.finance.yahoo.com/quote/'
    company = input("Enter the stock symbol, enter - if you want to remove a stock: ")
    while company != "":
        if company == "-":
            remove_company()
            break
        price = input("Enter the price you want to sell at: ")
        url = base_url + company
        urls.append(url)
        prices.append(price)
        company = input("Enter the stock symbol: ")
    for i in range(len(urls)):
        save_data(urls[i], prices[i])


def remove_company():
    remove = input("Enter the symbol of the company you want to remove: ")
    with open("stock_holds.txt", 'r+') as file_body:
        lines = file_body.readlines()
        for i in range(len(lines)):
            if remove in lines[i]:
                lines.pop(i)
                file_body.truncate(0)
                file_body.write("".join(lines))
                break


def save_data(stock, price):
    with open("stock_holds.txt", 'a') as file_body:
        lines = stock + " : " + price + '\n'
        file_body.write(lines)


add_a_stock()