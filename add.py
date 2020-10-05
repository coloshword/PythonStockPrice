def add_a_stock():
    global base_url
    urls = []
    prices = []
    base_url = 'https://ca.finance.yahoo.com/quote/'
    is_bought = bool(input("Enter True if you want to add a stock to watchlist: "))
    if is_bought:
        add_watchlist()
        return
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
        save_data("stock_holds.txt", urls[i], prices[i])


def add_watchlist():
    urls = []
    prices = []
    add_remove = input("Press enter if you want to add to the watchlist, - if you want to remove: ")
    if add_remove == "-":
        remove = True
    else:
        remove = False
    if remove:
        with open('stock_buys.txt', 'r+') as fh:
            lines = fh.readlines()
            for i in range(len(lines)):
                if remove in lines[i]:
                    lines.pop(i)
                    break
    if not remove:
        company = input("Enter the stock symbol, enter: ")
        while company != "":
            price = input("Enter the price you want to buy at: ")
            url = base_url + company
            urls.append(url)
            prices.append(price)
            company = input("Enter the stock symbol: ")
        for i in range(len(urls)):
            save_data('stock_buys.txt', urls[i], prices[i])


def remove_company():
    remove = input("Enter the symbol of the company you want to remove: ")
    with open("stock_holds.txt", 'r+') as file_body:
        lines = file_body.readlines()
        for i in range(len(lines)):
            if remove in lines[i]:
                lines.pop(i)
                break
    with open("stock_holds.txt", 'w+') as file_body:
        file_body.write("".join(lines))


def save_data(file, stock, price):
    with open(file, 'a') as file_body:
        lines = stock + " : " + price + '\n'
        file_body.write(lines)


add_a_stock()