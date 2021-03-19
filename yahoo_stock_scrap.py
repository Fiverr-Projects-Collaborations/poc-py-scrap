from pandas_datareader import data
stocks = ['GME', 'AMC']
for stock in stocks:
    stock_data = data.DataReader(stock, 'yahoo', '2021-01-01', '2021-01-31')
    print(stock_data)
    stock_data['symbol'] = stock
print(stock_data)
