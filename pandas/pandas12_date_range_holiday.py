import pandas as pd

df = pd.read_csv("date_range_holidays.csv")
print(df)

rng = pd.date_range(start="07-01-2017",end="07-31-2017",freq="B")
print(rng)

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
# from pandas.tseries.holiday import
usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng1 = pd.date_range(start="2017-07-01",end="2017-07-31",freq=usb)

df2 = df.set_index(rng1,inplace=True)                         #here 4-7-2017 is holiday in USA and by using this method we exclude in this date in dataframe
print(df)

# making customised calender
from pandas.tseries.holiday import AbstractHolidayCalendar,nearest_workday,Holiday


class MyBirthdayCalender(AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/
       snow-dismissal-procedures/federal-holidays/
    """

    rules = [
        Holiday("My birth day", month=6, day=25, observance=nearest_workday)]

# observance=nearest_workday  = if holiday is on weekend then nearest workday is called for holiday and declar as holiday
myc = CustomBusinessDay(calendar= MyBirthdayCalender())
print(pd.date_range(start="6/1/2022",end="6/30/2022",freq=myc))

# in Egypt weekend is friday and saturday           how to handle this situation

b = CustomBusinessDay(weekmask = "Sun Mon Tue Wed Thu ", holidays= ["2022-07-05"])
print(pd.date_range(start="7/1/2022",end="7/31/2022",freq=b))

c = CustomBusinessDay(weekmask = "Sun Mon",)
print(pd.date_range(start="7/1/2022",end="7/31/2022",freq=c))






