from functools import reduce
from itertools import accumulate


def add(a, b):
    return a + b


data = [25, 63, 89, 74, 22, 44, 96, 38, 56, 9, 45, 63]

result = reduce(add, data)
print("add data=", result)


def multiplication(a, b):
    return a * b


data1 = [9, 6, 8, 7, 6, 3, 1, 5, 6, 9, 9, 6, 8, 8]

result1 = reduce(multiplication, data1,100 )  # also we take initial(100) from that execution is start
print("multiplication data=",result1)

acc_result = list(accumulate(data, add))  # in accumulate first data after that function
print("accumulate data=",acc_result)  # in zip, ziplongest, filter, map and reduce first function then after data
#accumulate give succesive addition

# lambda function..................

x = lambda a, b: a + b
print(x(75, 25))

result = reduce(lambda a, b: a + b, data)
print(result)

acc_result = list(accumulate(data, lambda a, b: a + b))  # in accumulate first data after that function
print(acc_result)  # in zip, ziplongest, filter, map, reduce, first function after data

x = lambda a, b, c: a * b * c
print("lambda x=", x(2, 6, 3))

result2 = list(filter(lambda x: x if x % 2 == 0 else 0, data))    #ternery condition
print(result2)

dic = {56: 83, 24: 63, 89: 43, 78: 23}
d = sorted(dic.items())  # sorted according with key
sorted_dic = {key: value for key, value in d}  # dictionary comprehension
print(sorted_dic)

d = sorted(dic.items(), key=lambda x: x[1])  # sorted according with value
sorted_dic = {key: value for key, value in d}  # dictionary comprehension
print(sorted_dic)

data2 = [{"name": "xyz", "age": "30"}, {"name": "pqr", "age": "25"}, {"name": "abc", "age": "35"}]
d = sorted(data2, key=lambda x: x["age"])
print(d)

def sample_function(inf):
    return inf["name"]

a = sorted(data2, key=sample_function)                  #in key= we have to pass function--3
print(a)


