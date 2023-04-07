import datetime      #(full datetime module is imported)           # cls,c = class, v = variable , f = function
# from datetime import datetime -- (from datetime module only datetime function is imported)
# from datetime.datetime import now()   ---(only specific now function is imported)
# now                          # module = library = package are same    # standard = already installed in python
#  cls = accept class   self = accept object                             # non-standard = installed from outside (internet)
#### use for current time

date_now = datetime.datetime.now()                                      #(when, from datetime import datetime is use
print(date_now)                                                        #then date_now = datetime.now() this is code)

print(date_now.date())
print(date_now.time())
print(date_now.second)
print(date_now.hour)
print(date_now.minute)
print(date_now.day)
print(date_now.month)
print(date_now.year)

# for old datetime date and time object

back_dated = datetime.datetime(2022,1,22,5,5,25,25)             # positional
print(back_dated)
# back_dated = datetime.datetime(year= 1995,month= 6, day= 25, hour= 12, minute= 15, second= 25)         #keyword
# print(back_dated)
# back_dated = datetime.datetime(year= 1995,month= 6, day= 25)         #keyword
# print(back_dated)

# epochconverter.com for timestamp

# to timestamp

date_now_ts = date_now.timestamp()
back_dated_ts = back_dated.timestamp()
print(date_now_ts)
print(back_dated_ts)
print(datetime.datetime.now().timestamp())

# from timestamp
ts = 1664641508.054629
date_from_ts = datetime.datetime.fromtimestamp(ts)
print(date_from_ts)

# general introduction
# cls = have to pass any class or object         object= list[1,2,3] this is list object
# self = have to pass object

# strftime and strptime      (in communication time datetime is send in string)

# strftime --- convert datetime object to date string

format = "%d-%m-%Y %H:%M:%S"
dt_now = datetime.datetime.now()
str_dt = dt_now.strftime(format)
print(str_dt)
print(type(str_dt))
print("----------")

# strptime --- convert string to datetime object
dttime_str = "02-03-2022 07:14:23"
dt_frm_str = datetime.datetime.strptime(dttime_str, format)
print(dt_frm_str)
print(dt_frm_str.day) 
print(type(dt_frm_str))

'''
%a--	Abbreviated weekday name.--	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.	 
%Z	Time zone name.	 
'''
dt_now = datetime.datetime.now()

# combine --- which combine date and time to datetime
dt_date = dt_now.date()
dt_time = dt_now.time()
print(dt_date)
print(dt_time)

combine_dt = datetime.datetime.combine(dt_date,dt_time)
print(combine_dt)


# replace --- replace the value of date and time
replace_dt = combine_dt.replace(year=2021, month=4)
print(replace_dt)
replace_dt = dt_now.replace(year=2025)
print(replace_dt)

print("------")
print(dt_now.isoweekday())
print(dt_now.weekday())
print(datetime.datetime.utcnow())
print(dt_now.utcoffset())             # used to return a timedelta object that represents the difference betweeen the local
                                      # time and utc time.



