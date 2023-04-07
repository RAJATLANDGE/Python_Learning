import pandas as pd

dates = ["2017-01-05","Jan 5,2017","01/05/2017","2017.01.05","2017/01/05","20170105"]

dt = pd.to_datetime(dates)
print(dt)

dth = ["2017-01-05 2:30:00 pm","Jan 5,2017 14:30:00","01/05/2017","2017.01.05","2017/01/05","20170105","abc"]
dt = pd.to_datetime(dth, errors="coerce")                       #error= ignore, raise, coerce
print(dt)    #ignore= ignore the error  # raise = raise the error  # coerce = ignore the error element and perform rest of value

# usa mm/dd/yyyy erope dd/mm/yyyy             pycham yyyy/mm/dd
print(pd.to_datetime("5/1/2017"))
print(pd.to_datetime("5/1/2017",dayfirst=True))

print(pd.to_datetime("5$1$2017", format="%d$%m$%Y"))

#epoch(unix) time =  no. of second that have passed since jan 1,1970 00:00:00

t = 1656196534
date = pd.to_datetime([t],unit="s")          #here t is pass as array  result give datetimeindex
print(date)

print(date.view("int64"))             #convert datetimeindex to epoch time




