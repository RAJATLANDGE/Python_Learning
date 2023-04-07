import copy
# SHALLOW COPY = it only copies  outer object and copied references to the inner object , that's why when we change in innere
#                object then it also refert to the outer object.

original = [1, 2, 3, 4, 5]
copied = original.copy()                # this is called shallow copy
# copied = copy.copy(original)           # it also give shallow copy
print(original)
print(copied)
print("--------------")

copied.append(4)

print(original)
print(copied)
print("6----------------")

original1 = [{"day": "Wednesday", "date": "4th April"}, {"tomarrow": "Thrusday", "data": "5th April" }]
copied1 = original1.copy()

copied1.append({"dayafter":"friday", "date": "6th April"})
print(original1)
print(copied1)
print("5---------------")

copied1[1].update({"ocassion": "Akshay Tritiya"})
print(original1)
print(copied1)

print("4---------------")

#  Deep copy = first import copy model, it copies outer objects with all inner object with through all nested levels
#               it copies outer object and also copies inner object recursively
import copy

original2 = [{"day": "Wednesday", "date": "4th April"}, {"tomarrow": "Thrusday", "data": "5th April" }]

deep_copy = copy.deepcopy(original2)
print(deep_copy)
print("3---------------")

deep_copy.append({"dayafter":"friday", "date": "6th April"})
print(original2)
print(deep_copy)
print("2--------------")

deep_copy[1].update({"ocassion": "Akshay Tritiya"})
print(original2)
print(deep_copy)
print("1--------------")

data = [[1,2], [3,4],[5,6]]

d_copy = data.copy()
print(d_copy)
print(data)
print("--------------")

d_copy.append([6,7])
print(d_copy)
print(data)
print("--------------")

d_copy[1].append(9)        # shallow copy
print(d_copy)
print(data)
print("--------------")

import copy

data2 = [[1,2], [3,4],[5,6]]

d_copy2 = copy.deepcopy(data2)
print(data2)
print(d_copy2)
print("--------------")

d_copy2[1].append(10)            # deep copy
print(data2)
print(d_copy2)
print("--------------")
