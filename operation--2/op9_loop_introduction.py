# loop introduction
s = "hello"
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = (1, 2, 3)
d = {1:2, 3:4}
s1 = {1, 2, 3}

# syntex for forloop
# type_of_denomination
# recorded_data
# units
#
# for denomination in type_of_denomination:
#     pass
# for record in recorded_data:
#     pass
# for unit in units
#     pass

#  for general syntex for forloop
#  for item in range(-,-):

# for loop
num = list(range(1, 11))
for variable_name in num:
    if variable_name%2==0:
        print(f"{variable_name} ---> even")
    else:
        print(f"{variable_name} ---> odd")


print("for on string")
for item in s:
    print(item)
    print(item.upper())

print("for on list")
for item in l:
    print(item)

print("for on tuple")
for item in t:
    print(item)

print("for on ditionary")
for item in d:
    print(item)

print("for on set")
for item in s1:
    print(item)

print("values of dictionary")
for item in d.values():
    print(item)


# while loop (use when no data is present it run on condition not on data)

print("--------")
i = 1
while i<10:
    print("* "*i)
    i+=1

# expanded loop (for more than one variable is use e.g key and value variable is use in below)

print(d.items())

for key, value in d.items():
    print(f"{key} ---> {value}")

s1 = [85, 96, 78]
s2 = [75, 82, 94]
s3 = [79, 56, 68]

for s11, s22, s33 in zip(s1,s2,s3):
    print(f"student 1 mark in subject {s11}")
    print(f"student 2 mark in subject {s22}")
    print(f"student 3 mark in subject {s33}")


# for else loop

for item in l:
    print("do something")
    print("do other thing")
    break
else:
    print("do something when else")

for item in l:
    if item%5==0:
        break
    print(item)
else:
    print("loop exited after successful completion")             # when loop break else part not executed and viseversa

print("-----------------")

p = [1, 2, 3, 4, 6, 7, 8, 9]
for item in p:
    if item%5==0:
        break
    print(item)
else:
    print("loop exited after successful completion")



# while else loop

i = 0
while i<10:
    print("do something")
    i += 1
else:
    print("do something else")

num = 23
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print(f"{num} is prime")

def prime_finder(num):
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime number")
            break
    else:
        print(f"{num} is prime number")

prime_finder(22)