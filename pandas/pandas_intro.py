import numpy as np
import pandas as pd


dict = {"name": ["rohan", "harry", "shubham", "rajat"], "marks": [96, 85, 73, 81],
        "city": ["nagpur", "bangluru", "pune", "amravati"]}

df = pd.DataFrame(dict)  # (print the data in excel like format)
print(df)

# df.to_csv("friends.csv")                                              # (create excel file of given pass data)
df.to_csv("friend_index_false.csv", index=False)                        # (create excel file of given pass data without index)

print(df.head(2))                                                     #(show first two row )
print(df.tail(2))                                                     #(show last two row)
print(df.describe())                                                  #(show all statistical data of given numerical row)

read = pd.read_csv("rajat1.csv")                          #(read csv file)
print(read)

print(read["speed"])                                      #(read specific column)

read["speed"][0]= 100                                     #(change the specific values)
print(read["speed"])

read.to_csv("rajat1.csv")

read.index = ["first", "second", "third", "fourth"]
print(read)

series = pd.Series(np.random.rand(34))                                     #(give the series start from 0 to 33)
print(series)                                                              #series = column

print(type(series))                             #<class 'pandas.core.series.Series'>

dataframe = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))                        #dataframe = row
print(dataframe)
print(dataframe.head())
print(type(dataframe))                                                    #<class 'pandas.core.frame.DataFrame'>

print(dataframe.describe())
print(dataframe.dtypes)

print(dataframe.index)                                    #(give information about row(index))
print(dataframe.columns)                                  #(give information about columns)

print(dataframe.to_numpy())                                #convert pandas data into numpy data

print(dataframe.T)                                         #convert row to column and vice versa

print(dataframe.sort_index(axis=0, ascending=False))                                 #(axis=0 means row and axis=1 means column)

dataframe2 = dataframe.copy()                                            #making copy of data
dataframe.loc[0,2] = 5                                                               #[row,column]

print(dataframe.head(2))

dataframe.columns = list("ABCDE")
print(dataframe.head(2))
dataframe.loc[0,"C"] = 10
print(dataframe.head(2))

dataframe.loc[0,0] = 10                      #create new column
print(dataframe.head(5))
# dataframe.drop(df.columns[0],axis=1)
# print(dataframe.head(3))

print(dataframe.loc[[1,2],["C","D"]])                  #return specific pass values

print(dataframe.loc[[1,2],:])                           #return all column
print(dataframe.loc[:,["C","D"]])                       #return all rows

print(dataframe.loc[(dataframe["A"]<0.3)])                  #return only column "A" values with less than0.3

# print(dataframe.loc[(dataframe["A"]<0.3) and (dataframe["C"]>0.1)])

print(dataframe.iloc[0,4])                                   #return specific value
# iloc = only index number is pass,,, loc = specific column and row name is pass

print(dataframe.iloc[[0,4],[1,2]])

drop1 = dataframe.drop(["A"], axis=1)                        #drop only show copy of data does not change permenantly.
print(drop1)

dataframe.drop([0], axis=1, inplace=True)                   #inplace change the original data i.e, does not return copy
print(dataframe.head(2))

dataframe.drop([1,5], axis=0, inplace=True)
print(dataframe.head(10))

# dataframe.reset_index(drop=True, inplace=True)                     #reset index
# print(dataframe.head(6))


dataframe.loc[:,["E"]] = None                              #making specific value none or anything
print(dataframe.head(10))

dff = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),pd.NaT]})

print(dff)
print(dff.dropna())                             #delete none items
# print(df)
dup = dff.drop_duplicates(subset=["name"])
print(dup)

print(dff.shape)                                   # give dimention of given data

print(dff.info())                                 # give information of given data

cou = dff["toy"].value_counts(dropna=False)          #give the count of given values
print(cou)

isn = dff.isnull()                   #show null value as true and values as false
print(isn)
isnn = dff.notnull()                  # show null value as false  and values as true
print(isnn)

# data = pd.read_excel("data.xlsx")
# print(data)

con = df[df.marks>=90]
print(con)
abc = df[df.marks == df["marks"].max()]
print(abc)
ab = df[["name","city"]][df.marks == df["marks"].max()]
print(ab)


with pd.ExcelWriter("friends_rajat1.xlsx") as writer:
    dict.to_excel(writer,sheet_name= "friend")
    dff.to_excel(writer, sheet_name = "rjt1")



