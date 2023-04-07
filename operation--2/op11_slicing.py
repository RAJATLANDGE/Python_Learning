

     #   0  1  2  3  4   5   6    7    8    9    10     11   12
sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
     # -13-12-11-10 -9 -8  -7   -6   -5  -4    -3     -2   -1

print(sizes)

slice_data = sizes[4:8:1]
print(slice_data)
print(sizes[5])
print(sizes[5:9])
print(sizes[3:9:2])
print(sizes[3::2])
print(sizes[3::1])
print(sizes[:9:2])
print(sizes[::3])
print(sizes[::4])
print(sizes[::5])
# print(si)





print(sizes[7:9])
print(sizes[4:11:2])
print(sizes[1::3])
print(sizes[4:11:1])
# print(sizes[4:5:])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])
# print(sizes[::])

print("*****************")
recorded_data = ["sysinfo", "time", "machine info", "memory utilization", "user", "email", "roll", "total time"]
recorded_data1 = ["sysinfo", "time", "machine info", "memory utilization", "user", "email", "roll"]
student_marks = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 85]
sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
slice_object = slice(3,9,1)               #this is DRY = DONOT REPEAT YOURSELF

print(sizes[slice_object])
print(recorded_data[slice_object])
print(recorded_data1[slice_object])
print(student_marks[slice_object])







