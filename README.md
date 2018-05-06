# binance_data_analysis_stack
store and analyze binance crytocurrency exchange trade data.

## Roadmap:
1. tectonicdb initial test, store only btcusdt trade tick data [100%]
2. tectonicdb stress test, store all trade pairs [100%]
3. tectonicdb custom datastore format, to allow more info per row [10%]
4. store orderbook at any moment [0%]
5. map tectonicdb datastore into traditional database, allow time search [0%]
6. use plotly dash to visualize data [0%]
7. spin up server to host database [0%]
8. chaos engineering and fault tolerance [0%]
9. backup server [0%]
10. docker image [0%]
11. ml or dl to analyze data [0%]

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

#### this repo
clone this repo

#### setup git-secret
http://git-secret.io/

export gpg key: https://askubuntu.com/questions/648857/how-to-share-the-public-openpgp-key-using-gnupg

## Tech stack

#### 1. tectonicdb: https://github.com/rickyhan/tectonicdb
Remember to set tectonicdb upload to gcloud delete after upload to false


#### 2. fastai: https://github.com/fastai/fastai
For python environment, I just use the same as fastai, I find the script for setting up conda env extremely easy to use, and basically for any data science project, you have almost all the libraries that you will need.

#### 3. git-secret: http://git-secret.io/
Use this to store your api keys

#### 4. Dash by Plotly https://plot.ly/products/dash/
