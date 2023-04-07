import pandas as pd

# reshape dataframe using
# melt

df = pd.read_csv("pandas_melt.csv")
print(df)

df1 = pd.melt(df,id_vars="day")                               #id_vars =(id variable) thing that are unchange
print(df1)
# df1[df1["variable"]=="chicago"]
# print(df1)

df1 = pd.melt(df,id_vars="day", var_name = "city", value_name="temperature")          # change the variable and value columns name
print(df1)

