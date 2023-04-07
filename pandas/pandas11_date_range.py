import pandas as pd

df = pd.read_csv("NDHistoricalPrices.csv")
print(df.head())

rng = pd.date_range(start="6/1/2017",end="6/30/2017",freq="B")    #B=business days ie mon to fri
print(rng)

df.set_index(rng, inplace=True)                          #inplace modify the original data
print(df)

print(df["2017-06-01":"2017-06-10"])                     #get partial data frame

""""D" daily data "pad"= padding method which carry forward previour value to empty set 
as our original data frame does not have weekend dates so in "D" weekend date include and value of previous element is carry
 forward this is padding method  //// this is done using pandas asfreq function--3"""
print(df.asfreq("D", method="pad"))

#when we dont have end date
rng1 = pd.date_range(start="1/1/2017",periods=72,freq="B")    # give 72 dates starting with 1st january
print(rng1)

import numpy as np

print(np.random.randint(1,10,len(rng1)))                          # gives random number between 1 to 10, len(rng1)= 72

ts = pd.Series(np.random.randint(1,10,len(rng1)),index= rng1)      #give random number with index using in generate random data
print(ts.head(10))

