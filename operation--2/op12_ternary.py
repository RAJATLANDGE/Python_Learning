# ternary condition

# synthax
#         <somecode> if condition else <somecode>

print("even") if 9%2==0 else print("odd")

# both above and below code are same but in different synthex

if 9%2==0:
    print("even")
else:
    print("odd")


recorded_data = ["sysinfo", "time", "machine info", "memory utilization", "user", "email", "roll", "total time"]
recorded_data1 = ["sysinfo", "time", "machine info", "memory utilization", "user", "email", "roll"]
student_marks = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 85]
sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
slice_object = slice(3, 9, 1)

def func1():
    print(sizes[slice_object])
    print(recorded_data[slice_object])
    print(recorded_data1[slice_object])
    print(student_marks[slice_object])

def func2():
    print(recorded_data[slice_object])
    print(recorded_data1[slice_object])
    print(student_marks[slice_object])
    print(sizes[slice_object])

func1() if 10%2==0 else func2()

n = 55
(print("greater than 10 and even") if n>10 else print("less than 10 and even")) if n%2==0 else (print("greater than 10 and odd") if n>10 else print("less than 10 and odd"))