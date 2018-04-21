# binance_data_analysis_stack
store and analyze binance crytocurrency exchange trade data.

## Roadmap:
1. tectonicdb initial test, store only btcusdt trade data [100%]
2. tectonicdb stress test, store all trade pairs [100%]
3. tectonicdb custom datastore format, to allow more info per row [10%]
4. map tectonicdb datastore into traditional database, allow time search [0%]
5. use plotly dash to visualize data [0%]
6. spin up server to host database [0%]
7. chaos engineering and fault tolerance [0%]
8. backup server [0%]
9. docker image [0%]
10. ml or dl to analyze data [0%]

## Tech stack

#### 1. tectonicdb: https://github.com/rickyhan/tectonicdb
Remember to set tectonicdb upload to gcloud delete after upload to false


#### 2. fastai: https://github.com/fastai/fastai
For python environment, I just use the same as fastai, I find the script for setting up conda env extremely easy to use, and basically for any data science project, you have almost all the libraries that you will need.

#### 3. git-secret: http://git-secret.io/
Use this to store your api keys

#### 4. Dash by Plotly https://plot.ly/products/dash/
