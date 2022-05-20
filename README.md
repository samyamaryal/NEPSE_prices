# NEPSE_prices
Repo containing code that fetches stock prices from NEPSE's old website. 

The file nepalistocks.py contains code that fetches stock prices from NEPSE's old website. 
I tried fetching data from the new website (newweb.nepalstock.com.np), but an error related to SSL cert occured & I couldn't fix it.

The initial commit only fetches data from the first 20 stocks listed in alphabetical order.
This is because to load more prices, I'll need to write a code that automates request to load more prices.
(The URL for prices of 20 & 500 stock prices are surprisingly the same)
