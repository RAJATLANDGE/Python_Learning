import pandas as pd

#datetimeindex
df = pd.read_csv("HistoricalPrices.csv",parse_dates=["Date"],index_col="Date")
print(df.head(5))

print(df.index)                  #give the datetimeIndex of above data which data column is index

print(df.loc["2017-01"])              #here we can retrive only jan-2017 data from df.

print(df.loc["2017-01-01":"2017-01-07"])                # here we can retrive only in between pass date

headername = [ "Open",  "High",  "Low",  "Close",  "Volume"]
df.columns = headername

print(df.loc["2017-01"].Close.mean())

print(type(df["Close"]))

print(df.head(5))


# resampling
import matplotlib_inline

print(df.Close.resample("W").mean())                       #if we want chart then write .plot(kind= "bar")

