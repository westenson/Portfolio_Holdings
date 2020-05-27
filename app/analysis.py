import pandas as pd

import bs4 as bs
# import urllib.request
# !pip install yfinance
import yfinance as yf

def get_etf_holdings(etf_symbol, shares):
    
    #read the top 25 holdings in data frame
    dfs = pd.read_html("https://ycharts.com/companies/{}/holdings".format(etf_symbol),header=0)
    holdings = dfs[0]
    
    holdings.drop(["% Chg", "Price"], inplace=True, axis=1)

    #get etf price from most recent close
    etf_info = yf.Ticker(etf_symbol)
    etf_price = etf_info.info["previousClose"]
  
    #convert weight to float
    holdings["% Weight"] = holdings["% Weight"].str.rstrip("%")
    holdings["% Weight"] = holdings["% Weight"].astype('float') 
    
   
    #calculate $ owned 
    holdings["Amount Owned"] =  shares * etf_price * (holdings["% Weight"] / 100)
    
    holdings.drop(["% Weight"], inplace=True, axis=1)

    return(holdings)

def get_overall_holdings(etf_param_dict):
  print(etf_param_dict)
  ret = pd.DataFrame(columns=["Symbol", "Name", "Amount Owned"])
  for key, value in etf_param_dict.items():
    # print(get_etf_holdings(key, value))
    ret = ret.append(get_etf_holdings(key, value))
  
  ret = ret.groupby(by="Symbol").sum()

  print(ret.sort_values(by="Amount Owned", ascending=False, kind='mergesort'))

  return ret.sort_values(by="Amount Owned", ascending=False, kind='mergesort')
