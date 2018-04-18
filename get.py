from io import StringIO

from tectonic import TectonicDB
import pandas as pd

def get():
    db = TectonicDB()
    print (db.cmd("USE binance_btc_usdt")[1])
    data = db.cmd("GET ALL FROM 1514764800 TO 1514851200 AS CSV\n")[1]
    # data = db.cmd("GET ALL FROM 1514764800 TO 1514764860 AS CSV\n")[1]
    csv = StringIO("ts,seq,is_trade,is_bid,price,size\n"+data)
    df = pd.read_csv(csv)
    print (df)


if __name__ == '__main__':
    get()
