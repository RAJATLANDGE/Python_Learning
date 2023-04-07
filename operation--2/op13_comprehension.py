# comprehension = is short hand way to creat list, set, dict.
#  list comprehension
# [<variable_name> for <same variable_name> in iterator]
list100 = [item for item in range(1,101)]
print(list100)
even_list = [num for num in range(1,101) if num%2==0]
print(even_list)
odd_list = [nums for nums in range(1,101) if nums%2==1]
print(odd_list)

even_list = []
for num in range(1, 101):
    if num%2==0:
        even_list.append(num)
print(type(even_list))

# set comprehension

set_c = {item for item in range(1,101)}
print(set_c)


# dictionary comprehension

dict_c = {key:value for key,value in enumerate(even_list, 0)}
print("dict_c",dict_c)

dict_c2 = {key:key for key in range(0, 11)}
print(dict_c2)

# e.g
ascii_dict = {key:ord(str(key)) for key in range(0,10)}
print("ascii_dict",ascii_dict)
