import pandas as pd

# merge use when both dataframe has same element(eg city) name otherwise merge only merge the common element.
# and when all element require how= outer-> outer join can give all element
df1 = pd.DataFrame({"city":["new-york","chicago","orlando","baltimore"],"temperature": [21,14,35,32]})
print(df1)

df2 = pd.DataFrame({"city":["chicago","new-york","san francisco"],"humidity": [65,68,75]})
print(df2)

df3 = pd.merge(df1,df2,on="city",how="outer")
print(df3)

df4 = pd.merge(df1,df2,on="city")                  # here default is how = inner-join
print(df4)

df5 = pd.merge(df1,df2,on="city",how="left")
print(df5)

df6 = pd.merge(df1,df2,on="city",how="right")
print(df6)

df7 = pd.merge(df1,df2,on="city",how="outer",indicator= True)        #indicator show from where data is come from
print(df7)

df8 = pd.DataFrame({"city":["new-york","chicago","orlando","baltimore"],"temperature": [21,14,35,38], "humidity": [65,68,71,75]})
print(df8)

df9 = pd.DataFrame({"city":["chicago","new-york","san-diago"],"temperature": [21,14,35], "humidity": [65,68,71]})
print(df9)

df10 = pd.merge(df8,df9,on= "city",how = "outer")     # in result _x,_y is suffix
print(df10)

df11 = pd.merge(df8,df9,on= "city",how = "outer", suffixes=("_left","_right"))
print(df11)

