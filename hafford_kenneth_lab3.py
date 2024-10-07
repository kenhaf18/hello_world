from stock_data import STOCK_DATA # <- No touchy!


## a nested dictionary of STOCK_DATA, you may delete, modify, or use as is
stock_dict = dict()
for stock in STOCK_DATA:
    stock_dict[stock["symbol"]] = stock


# Below is ample code so you can see how to access nested dictionary keys. 
# You can delete this too if you don't need it!
for ticker in stock_dict.keys():
    print(ticker, ": ", stock_dict[ticker]["company"]) # ticker is the same as "symbol"
print("\n\n\n")
print(stock_dict["MMM"])
print(stock_dict["MSFT"]["initial_price"])

stock_dict = dict()
for stock in STOCK_DATA:
    stock_dict[stock['symbol']] = stock

stock_samples = dict()
for stock in STOCK_DATA[:4]:
    stock_samples[stock["symbol"]] = stock

stock_samples["DIS"]["initial_price"]

# 1. Print the difference between the 2007 price of each stock and the 2002 price. 
# Use conditional logic to indicate with a print statement whether the stock price went up or down.
#### ADD CODE HERE

def format_price(price):
    return (f"${round(price_diff)}\n")
mmm = stock_samples["MMM"]
price_diff = mmm["price_2007"] - mmm["price_2002"]
format_price(price_diff)

for symbol, value in stock_samples.items():
    # print(f"key is :{k}, values is {v.keys()}")
    print(f"{symbol} The price difference from 2007 - 2002 is: ${value['price_2007']}\n")

if mmm(price_diff) > 0:
    print ("The price went up")
else: 
    print ("The price went down")

#### 
# 2. What is the average initial price of all of the companies? 
#### ADD CODE HERE
initial_prices = []
for symbol, value in stock_samples.items():
    print(value["initial_price"])
    initial_prices.append(value["initial_price"])

avg_initial_price = sum(initial_prices) / len(initial_prices)
print(f"The average initial price is {avg_initial_price}")
####
# 3. Save all the stock tickers (The 3-5 letters labeled with "symbol" in each stock dictionary.) to a data structure, 
# you may choose the type (list, dictionary, tuple, string), sort the values to be in alphabetical order using Python. 
# Print all of the tickers in a loop, **two tickers per line.**
#### ADD CODE HERE

stock_tickers = ['MMM', 'AMZN', 'CPB', 'DIS', 'DOW', 'XOM', 'F', 'GPS', 'GIS', 'HPQ', 'IBM', 'JNJ', 'MSFT', 'MO', 'PEP', 'SBUX', 'TXN', 'TWX', 'UNH', 'WMT', 'WHL', 'XRX']
ordered_stock_tickers = sorted(stock_tickers)
print(ordered_stock_tickers)

i = 0

while i < len(stock_tickers):
    if i+1 < len(stock_tickers):
        print(stock_tickers[i], stock_tickers[i+1])
    else:
        print(stock_tickers[i]) 
    i += 2

#####
# 4. Which company name (not symbol) had the highest stock price in 2002? What is the lowest?
#### ADD CODE HERE

highest_stock_price = max(STOCK_DATA.items('price_2002'))
print(highest_stock_price)

####
#5. Which stock (company or symbol) had the smallest increase from their initial price to 2007? 
# (Decrease in price should not be counted.)
#### ADD CODE HERE

increased_stocks = [
    {
        "symbol": stock["symbol"],
        "company": stock["company"],
        "increase": stock["price_2007"] - stock["initial_price"]
    }
]
if increased_stocks:
    print(f'The smallest stock increase from initial price to 2007 ["company"]')
else:
    print(f'["company"] stocks did not have an increase from initial price to 2007.')