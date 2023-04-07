from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime

print(date.today())
print(date.min)
print(date.max)
today = date.today()
print(today.weekday())                   # weekday = 1st day is monday=0     (0 to 6)
print(today.isoweekday())                # isoweekday = 1st day is monday = 1,  sunday=7   (1 to 7)
print(today.strftime("%A %d-%m-%Y"))

# time

tt = time(12,12,45)
print(time.min)
print(time.max)
print(tt.strftime("%H:%M:%S"))
print(tt.replace(hour=11))

# timedelta

current_date = datetime.now()
past_date = datetime(1995,6,25)
print(current_date)
print('---------------')
print(current_date - past_date)
print(type(current_date - past_date))               #timedelta type

delta = timedelta(seconds = 5)                         #days seconds minute hours weeks milisecond microsecond in float
print(delta)

while True:
    if datetime.now() - current_date > delta:
        break
    import time
    time.sleep(2)
    print("**")

print("import time function--3 ")
import time      #( this is different from  <from datetime import time>) ( use for delay somethig)

time.sleep(5)
print("after sleep")

t1 = time.time()          #---------- start time
time.sleep(10)            # ---------- execute function--3
t2 = time.time()          # ---------- end time
print(f"slept for {t2 - t1}")         # give execution time for function--3