# builtins_functions

# dir(object)----------- to know what type of operation is done with the given object/datatype.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict1 = {1:2, 3:4, 5:6}

print("list dir", dir(list))
print("-------------")
print("dict dir", dir(dict))


# import requests
#
# response = requests.get("https://www.indiatoday.in/")
# print(dir(response))

# help ---
print(help(list1))

# divmod --- (quoant, remainder)
print(divmod(155,6))

def my_div_mod(dividend, divsor):
    quotient = dividend//divsor
    remainder =dividend%divsor
    return quotient, remainder
print(my_div_mod(155,6))

# frozenset -------- give set with no edits option (means give immutable set) i.e no .add option is present.
frozen_user_set = frozenset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(frozen_user_set)

# range
x = list(range(1,20,2))
y = list(range(78, 101))
print(x)
print(y)

for item in range(0, 10):
    print("*************")

print("--------------")

for i in range(1,11):
    print("* "*i)

# abs--- absolute value
print(abs(-9))
print(abs(5))
print(abs(5-10))
print(abs(2-3*10/5))

# bin --- to know binary digit of number

print(bin(9))
print(bin(7))
print(bin(-7))

# bool ---- converts the value to boolean

print("bool on string")
print(bool(111))
print(bool(0))
print(bool(""))
print(bool(" "))

print("bool on list")
print(bool([]))
print(bool([1, 2]))

# chr(number) --- give ascii table character
print(chr(99))
print(chr(66))
# ord ----- give ascii table number
print(ord("c"))
print(ord("B"))

# enumerate
data = [55, 66, 88, 77, 99, 12, 58, 63, "phone", "laptop" ]
d = list(enumerate(data, 1))
print(d)

for i, item in enumerate(data, 0):
    print(f"{item} is at index {i}")

# eval()------ give evaluated value of any no. or equation
print(eval("8*9+56"))

# hash -----  only immutable data is pass in hash
print(hash("s"))
# id --------- only immutable data is pass in id
print(id("s"))

# input --- it will take input from user, --- it will accept data only in string.
# input("enter a value")
# float(input("enter a average"))

# max and min
print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
print(min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

# oct and hex  --- octadecimal and hexadecimal
print(oct(10))
print(hex(10))

# pow --- power   (2**6)
print(pow(2,6))
print(2**6)

# round---  rounding of the value
print(round(7.6))
print(round(7.1))
print(round(7.5))
print(round(7.63))
print(round(7.68))

# sort--- sort the original data
n_data = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,32,33,34,98,75,88,42,69]

n_data.sort()
print(n_data)
n_data.append(55)
print(n_data)

# sorted---give sorted copy data without changing original data
n_data2 = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,32,33,34,98,75,88,42,69,88]

print(n_data2)
sorted_copy = sorted(n_data2, reverse=True)
print(sorted(n_data2, reverse=True))
sorted_copy.append(8956)
print(sorted_copy)
print(n_data2)

# sum --- sum of all element
print(sum([7,8,5,2,6,3,9,4]))

# import requests
#
# response = requests.get("https://www.google.co.in/")
# print(dir(response))
