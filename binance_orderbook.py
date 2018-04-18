from tectonic import TectonicDB
import json
import asyncio

# conf_scret is encrypted
from conf_secret import binance_pubkey, binance_prvkey

# binance stuff
from binance.client import Client
from binance.websockets import BinanceSocketManager
client = Client(binance_pubkey, binance_prvkey)

# Binance API
binance_api_struct = {
  "e": "aggTrade",  # Event type
  "E": 123456789,   # Event time
  "s": "BNBBTC",    # Symbol
  "a": 12345,       # Aggregate trade ID
  "p": "0.001",     # Price
  "q": "100",       # Quantity
  "f": 100,         # First trade ID
  "l": 105,         # Last trade ID
  "T": 123456785,   # Trade time
  "m": True,        # Is the buyer the market maker?
  "M": True         # Ignore.
}

db = TectonicDB()

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print(msg)
    # do something
    loop = asyncio.new_event_loop()
    loop.run_until_complete(add_msg_to_db(msg))

async def add_msg_to_db(msg):
    await db.add(msg['E'], msg['a'], not msg['m'], msg['m'], msg['p'], msg['q'])

def binance_tick():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(db.create('binance_btc_usdt'))
    loop.run_until_complete(db.use('binance_btc_usdt'))

    bm = BinanceSocketManager(client)
    bm.start_aggtrade_socket('BTCUSDT', process_message)
    bm.start()

if __name__=='__main__':
    binance_tick()
