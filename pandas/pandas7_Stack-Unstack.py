import pandas as pd

# df = pd.read_csv("stocks1.csv", header=[0,1])
# print(df)

df = pd.read_excel("stocks.xlsx", header=[0,1])
print(df)

df_stack = df.stack()             # stack take inner most header and  convert columns to row transformation
print(df_stack)

df2 = df.stack(level=0)            #zero index header transform row to column
print(df2)

df3 = df_stack.unstack()           # unstack convert vise versa of stack
print(df3)

df4 = pd.read_excel("stocks.xlsx", header=[0,1,2])
print(df4)

df5 = df4.stack(level=2)
print(df5)









