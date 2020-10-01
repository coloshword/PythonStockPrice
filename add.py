def add_a_stock():
    base_url = 'https://ca.finance.yahoo.com/quote/'
    company = input("Enter the stock symbol: ")
    url = base_url + company
    print(company)

add_a_stock()