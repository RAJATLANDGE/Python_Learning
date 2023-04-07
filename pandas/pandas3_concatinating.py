import pandas as pd

india_weather = pd.DataFrame({"city":["mumbai","delhi","banglore"],"temperature": [32,45,30], "humidity": [80,60,78]})
print(india_weather)

us_weather = pd.DataFrame({"city":["new-york ","chicago","orlando"],"temperature": [21,14,35], "humidity": [68,65,75]})
print(us_weather)

df = pd.concat([india_weather,us_weather])                     #join 2 or more dataframe
print(df)

df = pd.concat([india_weather,us_weather], ignore_index=True)     # using this ignor previous index and apply new
print(df)

df = pd.concat([india_weather,us_weather], keys=["india", "us"]) # by using this key after that we call that data by using this key
print(df)

print(df.loc["india"])      # call by using key

temperature_df = pd.DataFrame({"city":["mumbai","delhi","banglore"],"temperature": [32,45,30]}, index=[0,1,2])
print(temperature_df)

windspeed_df = pd.DataFrame({"city":["banglore","delhi"],"windspeed": [12,9]}, index=[2,1])
print(windspeed_df)

df = pd.concat([temperature_df,windspeed_df],axis=1)               #by using index help in concating data perfectly
print(df)

s = pd.Series(["humid","dry","rain"], name = "event")
print(s)

df = pd.concat([temperature_df,s], axis=1)
print(df)


