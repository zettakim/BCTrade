import time

import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']
asks = orderbook['asks']
print(bids)
print(asks)

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("매수호가: ", price, "매수잔량: ", quant)

for ask in asks:
    print(ask)

all = pybithumb.get_current_price("ALL")

for k, v in all.items():
    print(k, v)

for ticker, data in all.items():
    print(ticker, data['closing_price'])

while True:
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
    except:
        print("에러 발생", price)
    time.sleep(2)
