import pandas as pd
from pandas import DataFrame
import quandl
import pandas_datareader as web
from time import sleep
import datetime as dt
import sys
import  json
from datetime import datetime as dt, timedelta

def parseApis(sourceapi,tickers,start,end):
    sp500 = None
    missingTickers = []
    with open('config', 'r') as f:
        config = json.load(f)
    #tickers = ['AAPL', 'TSLA', 'YHOO','GOOG', 'MSFT','ALTR','WDC','KLAC','CTL']
    tickers = ['AAPL']
    quandl.ApiConfig.api_key = config['QuandlApiKey']

    for counter,s in enumerate(tickers):
            try:
                sleep(2)
                if sourceapi == "google" or sourceapi == "yahoo" :
                    s_data = web.DataReader(s, sourceapi, start, end).loc[:, ["Adj. Close", "Open"]]
                elif sourceapi == "Quandl":
                    s_data = quandl.get("WIKI/" + s, start_date=start, end_date=end).loc[:, ["Adj. Close", "Open"]]
                elif sourceapi == "custom":
                    pass
                s_data['Name'] = s
                s_data = s_data[['Name','Open','Adj. Close']]
                missingData = s_data[s_data.isnull()]
                s_data.dropna(how = "any" ,inplace = True )
                if s_data.shape[0] > 1:
                    if sp500 is None:
                        sp500 = DataFrame(s_data)
                    else:
                        sp500 = pd.concat([sp500 , s_data],axis=0)
                else:
                    missingTickers.append(s)

                print(" {} Retrival Done for {}".format(counter+1,s))
            except Exception as e:
                print("Excetion occured for Ticker : {}".format((s)))
                print(e)
                continue

    if type(sp500) != type(None):
        sp500.rename(columns={"Adj. Close":"Close" , "Open":"Open" } , inplace=True)
        sp500 = sp500.sort_index(ascending=False)
        sp500 = sp500[['Name','Open','Close']]
        return sp500
    print("Data For the following tickers is missing ".format(missingTickers))

