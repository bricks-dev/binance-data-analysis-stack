# binance_data_analysis_stack
store and analyze binance crytocurrency exchange trade data.

## Roadmap:
1. tectonicdb initial test, store only btcusdt trade tick data [100%]
2. tectonicdb stress test, store all trade pairs [100%]
3. tectonicdb custom datastore format, to allow more info per row [10%]
4. store orderbook at any moment [0%]
5. map tectonicdb datastore into traditional database, allow time search [0%]
6. use plotly dash to visualize data [0%]
7. spin up server to host database [100%]
8. chaos engineering and fault tolerance [0%]
9. backup server [0%]
10. docker image [0%]
11. ml or dl to analyze data [0%]
12. simple logging [100%]

## Installation AWS EC2
if you are on free tier, pick 30gb storage, the entire installation should take about 16gb
this gives you some leftover storage to store data
#### TectonicDB
```
sudo apt-get update
sudo apt-get upgrade
```
install rust: 
https://www.rust-lang.org/en-US/install.html

clone tectonicdb, my branch has google cloud upload turned off: 
https://github.com/mingrui/tectonicdb.git

master branch: https://github.com/rickyhan/tectonicdb

before building tectonicdb, install gcc: 
https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91
```
GCC 8.1.0 on Ubuntu 14.04 & 16.04 & 18.04:

sudo apt-get update -y && 
sudo apt-get upgrade -y && 
sudo apt-get dist-upgrade -y && 
sudo apt-get install build-essential software-properties-common -y && 
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y && 
sudo apt-get update -y && 
sudo apt-get install gcc-8 g++-8 -y && 
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 60 --slave /usr/bin/g++ g++ /usr/bin/g++-8 && 
sudo update-alternatives --config gcc

select gcc-8
```

Install OpenSSL, **after installation reboot EC2 instance**, otherwise OpenSSL path will not register.
https://github.com/sfackler/rust-openssl
```
sudo apt-get install pkg-config libssl-dev
```

Setup rust nightly: https://github.com/rust-lang-nursery/rustup.rs#working-with-nightly-rust

Build tectonicdb

#### Anaconda
install anaconda: https://conda.io/docs/user-guide/install/linux.html

#### fastai
mainly using this for the easy to use tools that come along with it.

https://github.com/fastai/fastai

#### python-binance
`source activate fastai`, then install this binance api helper
https://github.com/sammchardy/python-binance

#### this repo
clone this repo

#### setup git-secret
http://git-secret.io/

export gpg key: https://askubuntu.com/questions/648857/how-to-share-the-public-openpgp-key-using-gnupg

download key file from ec2: https://stackoverflow.com/questions/9441008/how-can-i-download-a-file-from-ec2

when creating a new gpg key on your aws, you need to use a **DIFFERENT** email address, otherwise `git secret reveal` will not work

To tell someone a secret, make sure you have gawk installed `sudo apt-get install gawk`

#### start binance_orderbook.py
remember to use fastai
`source activate fastai`

change liblibtectonic.so location to use absolute path, in ffi.py
`lib_path = path.normpath(path.join(cwd, '/mnt/960EVO/workspace/tectonicdb/target/debug/liblibtectonic.so'))`

`python binance_orderbook.py`

#### jupyter lab
install
https://github.com/jupyterlab/jupyterlab

to connect to jupyter lab running on ec2 instance
https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5

## Usage

For tectonic-server, i just set write intervalto 1000 rows / flush
(flush is tectonicdb's term for batch write operation)
`./tectonic-server -vv -a -i 1000`



## Tech Stack

#### tectonicdb: https://github.com/rickyhan/tectonicdb
Remember to set tectonicdb upload to gcloud delete after upload to false

#### python-binance: https://github.com/sammchardy/python-binance
binance websocket api

#### fastai: https://github.com/fastai/fastai
For python environment, I just use the same as fastai, I find the script for setting up conda env extremely easy to use, and basically for any data science project, you have almost all the libraries that you will need.

#### git-secret: http://git-secret.io/
Use this to store your api keys

#### Dash by Plotly https://plot.ly/products/dash/

## Dev Resources

| Topic | Link |
| ----- | ----- |
| Logging | https://logmatic.io/blog/python-logging-with-json-steroids/ |
| Logging | https://docs.python.org/3/howto/logging-cookbook.html |
| Logging | https://docs.python.org/3/howto/logging.html |
| api | https://sammchardy.github.io/binance/2018/01/08/historical-data-download-binance.html |
| DTF | https://www.martinseeler.com/developing-efficient-bianry-file-protocol-with-scodec-and-akka-streams.html |

## TectonicDB Improvements Proposals

```
//!
//! File format for Dense Tick Format (DTF)
//!
//!
//! File Spec:
//! Offset 00: ([u8; 5]) magic value 0x4454469001
//! Offset 05: ([u8; 20]) Symbol
//! Offset 25: (u64) number of records
//! Offset 33: (u32) max ts
//! Offset 80: -- records - see below --
//!
//!
//! Record Spec:
//! Offset 81: bool for `is_snapshot`
//! 1. if is true
//!        4 bytes (u32): reference ts
//!        2 bytes (u32): reference seq
//!        2 bytes (u16): how many records between this snapshot and the next snapshot
//! 2. record
//!        dts (u16): $ts - reference ts$, 2^16 = 65536 - ~65 seconds
//!        dseq (u8) $seq - reference seq$ , 2^8 = 256
//!        `is_trade & is_bid`: (u8): bitwise and to store two bools in one byte
//!        price: (f32)
//!        size: (f32)
```

1. Each `record` is ordered into rows, dts is u16, can store about 65 seconds. This might be problematic for infrequent token pairs. Need to insert empty rows if 65 seconds limit is reached.

2. Convert row datastore into column datastore
