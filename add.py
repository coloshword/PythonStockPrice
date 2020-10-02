def add_a_stock():
    urls = []
    base_url = 'https://ca.finance.yahoo.com/quote/'
    company = input("Enter the stock symbol: ")
    while company != "":
        url = base_url + company
        company = input("Enter the stock symbol: ")
        urls.append(url)
    for url in urls:
        save_data(url)


def save_data(text):
    with open("stock_dictionary.txt", 'a') as file_body:
        lines = text + '\n'
        file_body.write(lines)

add_a_stock()