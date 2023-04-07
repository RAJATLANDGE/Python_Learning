import pandas as pd

# df = pd.read_csv(pass csv file name)

# weather_data =  {python dictionary}
# df = pd.DataFrame(weather_data)

# df.shape  ----- return dimention of above dataframe in tuple (row,column)

# df.head() -------  return intial few rows or pass value in bracket for no. of rows you required, from above
# df.tail () ------- return intial few rows or pass value in bracket for no. of rows you required, from downword

# df[2:5]------ return row two to four
# df.columns ---- return column names

# df.<columns name>------return columns contain or df["<column name>"]

 # df[["<columns name>","<columns name>"]]       --- this way we return multiple columns

# df["<columns name>"].max()   --- give max value of pass column just that min, mean, std,

# df.describe()   ------ give description of table with men, std, min, max, count, etc of the column wihch have numerical values

# df[df.temperature >= 32] -----  give the rows which have temperature greater than equal to 32
#df[df.temperature == df.temperature.max()] ---- give the only row in which temperature is maximum
#df[df.temperature == df["temperature"].max()] -- or this

# df["day"][df.temperature == df["temperature"].max()]   ---this way we only print day which have maximum temperature
# df["day","temperature"][df.temperature == df["temperature"].max()] --- this way we print day and temperature of row
# which have max temperature

# default index is 0 to n

# df.set_index("day") ---- it set day column as index

# df.set_index("day", inplace = True) -- without inplace it extracts some data from original but does not
# change original dataframe, but when we use inplace it modifies original dataframe

#df.loc[1/3/2017]   -- by setting date as index now we extract data by using index as date

# df.reset_index(inplace=True) --  reset our original dataframe and return our original data with default index


# ##########--------different ways of creating dataframe---------#########

# 1) df= pd.read_csv("file name or file path")

# 2) df = pd.read_excel("file name or file path","sheet1")

# 3) df = pd.Dataframe(python dictionary)

#  4)
weather_data= [("1/1/2017",32,6,"rain"),("1/2/2017",35,7,"sunny"),("1/3/2017",28,2,"snow")]
df = pd.DataFrame(weather_data, columns=["day","temperature", "windspeed", "event"])
print(df)
############---------------------- read and write csv and excel files

# df = pd.read_csv("file_name",header/skiprows=1) -- for skip rows in csv file

# df = pd.read_csv("file_name",header=1,names=["a","b","C"]) ---- if no header (ie columns name) by this way we create
                                                                              # columns name

# df= pd.read_csv("file name or file path", nrows=3)---- read exactly pass no. of rows only, from all large data

# df= pd.read_csv("file name or file path", na_values= ["not available","n.a."])--- pass values are in csv files is replace by NaN
# ie "not available" by this way we can replace the not required or missing values is replace by NaN by na_values artribute

# df= pd.read_csv("file name or file path", na_values= {"column_name": ["not available","n.a."],"column_name":"-1"})
# if you want to specific columns value is replace with NaN then we pass dictionary in na_values

# df.to_csv("new_file_name")         ----to save above "df" csv file as new_file_name -- at save automatic index is also save
# df.to_csv("new_file_name",index=False,header= False) ----- at time of saving to avoiding index, pass index equal to False
                                               # and if you did not want header in save file then pass header equal to false
# df.to_csv("new_file_name",columns=["columns_names","columns_name"]) --- at the time of save csv file, if you want only few
                                        # columns are save in file then columns= parameter is pass with required columns names

# df= pd.read_excel("<file_name or file path","sheet1")

# df.to_excel("new.xlsx",sheet_name="stocks",startrow=1,startcol=2)   -- to save above excel file as new.xlsx and other
# function is same for excel and save in excel start at row=1 and column=2

# two dataframe as df_stocks and df_weather

# with pd.ExcelWriter("stocks_weather.xlsx") as writer:  -------to save to excel file in one excel file at different sheet
#     df_stocks.to_excel(writer,sheet_name="stocks")
#     df_weather.to_excel(writer,sheet_name="weather")

#############     handling  missing data



