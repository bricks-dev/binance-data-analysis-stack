from io import StringIO

from tectonic import TectonicDB
import pandas as pd

import asyncio

async def get():
    db = TectonicDB('ec2-54-70-231-109.us-west-2.compute.amazonaws.com')
    print(await db.ping())
    # print( await db.cmd('USE {}'.format('ethbtc@trade')) )
    # data = await db.cmd("GET ALL FROM 1514764800 TO 1514851200 AS CSV\n")
    # print(data)
    # data = db.cmd("GET ALL FROM 1514764800 TO 1514764860 AS CSV\n")[1]
    # csv = StringIO("ts,seq,is_trade,is_bid,price,size\n"+data[1].decode())
    # df = pd.read_csv(csv)
    # print (df)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(get())
    loop.run_forever()
    loop.close()
