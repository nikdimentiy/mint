import csv

with open("quotes.csv") as data_file:
    data = csv.reader(data_file)
    stock_price = []
    for row in data:
        if row[1] != "Current Price":
            stock_price.append(float(row[1]))
    print(stock_price)
    total_sum = 0
    for i in stock_price:
        total_sum += i
    print(total_sum)
    print(max(stock_price))
