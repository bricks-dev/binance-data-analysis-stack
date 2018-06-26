#!/usr/bin/env python

from conf_secret import binance_pubkey, binance_prvkey

from binance.websockets import BinanceSocketManager

from binance.client import Client
client = Client(binance_pubkey, binance_prvkey)

time_res = client.get_server_time()

RECV_WINDOW=6000000

class Monitor:
    def __init__(self):
        self.bac = Client(binance_pubkey, binance_prvkey)
    def my_balance(self):
        print(self.bac.get_all_tickers())


m = Monitor()
m.my_balance()






def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something


bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_symbol_ticker_socket('BNBBTC', process_message)
# then start the socket manager
bm.start()


