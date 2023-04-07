# implicit type conversion

sum = 5 + 8.5
print(type(sum))


# explicit type conversion
print("float to integer conversion")
avg = 89.65
num = 5
print(type(avg))

int_avg = int(avg)      #or int_avg = int(89.56)
print(type(int_avg))
print(int_avg)

str_num = str(num)
print(str_num)

str_flo = str(avg)
print(str_flo)
print(type(str_flo))



print("string to integer and float conversion ")
contact = "8055886898"
print(type(contact))

tuple_con = tuple(contact)
print(type(tuple_con))
print(tuple_con)

int_con = int(contact)
print(type(int_con))
print(int_con)

float_con = float(contact)
print(type(float_con))
print(float_con)


print("string to list and set conversion")
list_con = list(contact)
print(type(list_con))
print(list_con)

set_con = set(contact)
print(type(set_con))
print(set_con)

dict_con = dict().fromkeys(contact)
print(type(dict_con))
print(dict_con)

print("list conversion")
sample_list = ["a", "b", "asd", "dy", "erop"]

set_list = set(sample_list)
print(type(set_list))
print(set_list)

dict_list = dict().fromkeys(sample_list)
print(type(dict_list))
print(dict_list)

str_list = "".join(sample_list)
print(type(str_list))
print(str_list)

tuple_list = tuple(sample_list)
print(type(tuple_list))
print(tuple_list)

print("set conversion")
set_data = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

list_set = list(set_data)
print(type(list_set))
print(list_set)

dict_set = dict.fromkeys(set_data)
print(type(dict_set))
print(dict_set)

str_set = "".join(set_data)
print(type(str_set))
print(str_set)

tuple_set = tuple(set_data)
print(type(tuple_set))
print(tuple_set)

tuple_data = ('monday', 'tuesday', 'wednesday', 'thusday', 'friday', 'saturday', 'sunday')

list_tuple = list(tuple_data)
print(type(list_tuple))
print(list_tuple)

dict_tuple = dict.fromkeys(tuple_data)
print(type(dict_tuple))
print(dict_tuple)

str_tuple = "".join(tuple_data)
print(type(str_tuple))
print(str_tuple)

set_tuple = set(tuple_data)
print(type(set_tuple))
print(set_tuple)