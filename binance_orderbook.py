import asyncio
import logging

from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.depthcache import DepthCacheManager
from binance.enums import *

from tectonic import TectonicDB

from conf_secret import binance_pubkey, binance_prvkey


'''
tectonic db row format
(timestamp, seq, is_trade, is_bid, price, size)
ts: Timestamp of the order received by client.
seq: Sequence number to re-order the events received.
size: Order size
price: Price of order
is_bid: Is the order a buy or sell
is_trade: Is it a market order or limit order

binance trade stream format
{
  "e": "trade",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "t": 12345,       // Trade ID
  "p": "0.001",     // Price
  "q": "100",       // Quantity
  "b": 88,          // Buyer order Id
  "a": 50,          // Seller order Id
  "T": 123456785,   // Trade time
  "m": true,        // Is the buyer the market maker?
  "M": true         // Ignore.
}

https://github.com/sammchardy/python-binance
'''

# simple logging
logging.basicConfig(filename='binance-tectonicdb-test.log', level=logging.INFO, format='%(asctime)s %(message)s')

# binance client
client = Client(binance_pubkey, binance_prvkey)
# connect to tectonicdb
db = TectonicDB()
# use only one event loop
loop = asyncio.get_event_loop()

def process_depth(depth_cache):
    if depth_cache is not None:
        print("symbol {}".format(depth_cache.symbol))
        print("top 5 bids")
        print(depth_cache.get_bids()[:5])
        print("top 5 asks")
        print(depth_cache.get_asks()[:5])
    else:
        # depth cache had an error and needs to be restarted
        pass

def process_message(msg):
    print(msg)

# get binance orderbook stack to find out whether trade is market order or limit order
def orderbook_depth():
    #dcm = DepthCacheManager(client, 'BNBBTC', callback=process_depth, refresh_interval=0)

    bm = BinanceSocketManager(client)
    #diff_key = bm.start_depth_socket('BNBBTC', process_message)
    partial_key = bm.start_depth_socket('BNBBTC', process_message, depth=BinanceSocketManager.WEBSOCKET_DEPTH_5)
    bm.start()

def process_m_message(msg):
    stream = msg['stream']
    data = msg['data']
    print("stream: {} data: {}".format(stream, data))
    loop.run_until_complete(db.insert(data['E'], data['t'], True, data['m'], data['p'], data['q'], stream))

def multiplex_sockets(tickers):
    for tic in tickers:
        logging.info('start collecting tic : ' + tic)
        loop.run_until_complete(db.create(tic))

    bm = BinanceSocketManager(client)
    conn_key = bm.start_multiplex_socket(tickers, process_m_message)
    bm.start()

if __name__=='__main__':
    logging.info('start')
    all_tickers = [tic['symbol'].lower() for tic in client.get_all_tickers()]
    multiplex_sockets([tic+'@trade' for tic in all_tickers])

    #orderbook_depth()
