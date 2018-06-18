from conf_secret import binance_pubkey, binance_prvkey

from binance.client import Client
client = Client(binance_pubkey, binance_prvkey)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')
# get all symbol prices
prices = client.get_all_tickers()

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()
