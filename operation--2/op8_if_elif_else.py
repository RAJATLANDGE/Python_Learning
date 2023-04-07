
print(1)
if True:
    print("*****")
    print(2)
    print(3)
    print(4)
print(5)

if False:
    print("#####")
    print(6)
    print(7)
print(8)

if True:
    print("if block")
    print(11)
    print(12)
    print(13)
else:                                       # no gap between if last block and else function--3
    print("else block")
    print(14)
    print(15)

num = int(input("Emter A Number"))

if num%2==0:
    print("even")
else:
    print("odd")

if "monday".endswith("day"):
    print("yes")
else:
    print("No")

avg = float(input("enter your average"))

if avg >= 90:
    print("Toppers")
elif avg >= 75:
    print("Distinction")
elif avg >= 60:
    print("first class")
elif avg >= 50:
    print("second class")
elif avg >= 40:
    print("pass class")
else:
    print("Fail")


day = input("enter a day").lower()

if day.startswith("mon") and day.endswith("day"):
    print("this is the first day of week")
elif day.startswith("tue"):
    print("this is the second day of week")
elif day.startswith("wed"):
    print("this is the third day of week")
elif day.startswith("thus"):
    print("this is the fourth day of week")
elif day.startswith("fri"):
    print("this is the fifth day of week")
elif day.startswith("sat"):
    print("this is the sixth day of week")
elif day.startswith("sun"):
    print("this is the seventh day of week")
else:
    print("given day is not a valid day")

if True:
    print(21)
    print(22)
    if True:
        print(23)
        print(24)
    print(25)

if True:
    print(26)
    print(27)
    if False:
        print(28)
        print(29)
    print(30)