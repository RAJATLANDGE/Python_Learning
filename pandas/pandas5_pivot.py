import pandas as pd
# pivot and pivot table
# pivot allow you to transform or reshape data
# pivot table allow you to summerize and aggregate data inside dataframe
df = pd.read_csv("Tutorial 8-pivot.csv")
print(df)

df1 = df.pivot(index="day", columns="city")                    #index = row
print(df1)

df2 = df.pivot(index="day", columns="city",values= "humidity")
print(df2)

df3 = pd.read_csv("weather 2.csv")
print(df3)

df4 = df3.pivot_table(index="city", columns="day")         #give aggregate of value of both date # mean is default
print(df4)

df5 = df3.pivot_table(index="city", columns="day", aggfunc="sum",margins=True)  # in aggfunc we use count, sum, etc
print(df5)

df6 = df3.pivot_table(index="city", columns="day", margins = True)   # margins give mean of row and columns as -> All
print(df6)

df7 = pd.read_csv("weather 3.csv")
print(df7)

df7["day"] = pd.to_datetime(df7["day"])
print(type(df7["day"][0]))
print(df7)

df8 = df7.pivot_table(index=pd.Grouper(freq="M",key="day"),columns="city")
print(df8)

# grouper function give average according with value pass in freq.
# M = months   key = where average is calculate





