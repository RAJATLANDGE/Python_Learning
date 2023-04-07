import pandas as pd
import numpy as np

df1 = pd.read_csv("Tutorial 5-handing missing data.csv",parse_dates=["day"]) # change type of day column as timestamp by parse_dates
print(type(df1.day[0]))
df1.set_index("day",inplace=True)
print(df1)

# new_df = df1.fillna(0)                   #replace NaN as pass value
# new_df = df1.fillna({"temperature":0,"windspeed":0,"event":"no event"})     #replace with specialise column values
# new_df = df1.fillna(method="ffill")                #ffill= carry forward, the value of previous row to next row if row is NaN
                                 #bfill = carry forward backword also pass bfill in method
# new_df = df1.fillna(method="ffill",axis="columns")     #it fill NaN value ie carry forward by rows-wise
# new_df = df1.fillna(method="ffill",limit=1)  #carry forward limit is 1 hence when two NaN is present then only one Nan is carry
                                                    # forward with above value but 2nd NaN is leave
new_df = df1.interpolate(method="time")           #fill NaN values as average of above and below values
 #here 2nd and 3rd date is missing thus avg accuracy is not perfect for perfection value is near to 4th hence method= time is use
# print(new_df)

####DROP NA
# new_df= df1.dropna()                                 # drop all row which NaN
# new_df= df1.dropna(how="all")                      # drop row if all row is contain NaN
# new_df= df1.dropna(thresh=1)                       #drop only row which does not have any valid value( other than NaN)
# print(new_df)


# inserting missing date
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df2 = df1.reindex(idx)
print(df2)



print("----------------**************************--------------------------")

df = pd.read_csv("Tutorial 6-replace.csv")
print(df)

# new_df = df.replace([-99999,-88888], np.NAN)
# print(new_df)

new_df = df.replace({"temperature":-99999, "windspeed": [-99999,-88888], "event":"0"}, np.NAN)
print(new_df)

new_df = df.replace({-99999: np.NaN, "no event": "Sunny"})          #by using mapping method
print(new_df)

new_df = df.replace({"temperature":"[A-Za-z]","windspeed":"[A-Za-z]"},"", regex=True)
print(new_df)

df2 = pd.DataFrame({"score": ["exceptional", "average", "good", "poor","average","exceptional"],
                              "student": ["rob", "maya", "parthiv", "tom", "julian", "erica"]})
print(df2)

new_df2 = df2.replace(["exceptional", "good", "average", "poor"], [4,3,2,1])
print(new_df2)







