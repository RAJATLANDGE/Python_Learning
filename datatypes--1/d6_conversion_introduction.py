# implisite type conversion  ----- who convert one type of data to another one automatically
# e.g
sum = 5+10.5
print(type(sum))

# explisite type conversion
# float to integer
avg = 85.96
int_avg = int(avg)
print(type(avg))
print(type(int_avg))
print(int_avg)

# string conversion

contact = "8055886898"
print(type(contact))
con_int = int(contact)
print(type(con_int))
print(con_int)

con_float = float(contact)
print(type(con_float))
print(con_float)

con_list = list(contact)
print(type(con_list))
print(con_list)

con_set = set(contact)
print(type(con_set))
print(con_set)

con_dict = dict.fromkeys(contact)
print(type(con_dict))
print(con_dict)

con_tuple = tuple(contact)
print(type(con_tuple))
print(con_tuple)

# list conversion

sample_list = ["qm", "lm", "qw", "rr", "mj", "bn", "rt", "ku", "hg", "a", "B"]
print(type(sample_list))

set_list = set(sample_list)
print(type(set_list))
print(set_list)


dic_list = dict.fromkeys(sample_list)
print(type(dic_list))
print(dic_list)

str_list = "".join(sample_list)
print(type(str_list))
print(str_list)

tup_list = tuple(sample_list)
print(type(tup_list))
print(tup_list)

# set conversion
set_data = {'1','2','3','4','5'}

list_set = list(set_data)
print(type(list_set))
print(list_set)

str_set = "".join(set_data)
print(type(str_set))
print(str_set)

dict_set = dict.fromkeys(set_data)
print(type(dict_set))
print(dict_set)

tup_set = tuple(set_data)
print(type(tup_set))
print(tup_set)

# tuple conversion

tuple_data = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'july', 'aug', 'sept', 'oct', 'nov', 'dec')

list_tup = list(tuple_data)
print(type(list_tup))
print(list_tup)

set_tup = set(tuple_data)
print(type(set_tup))
print(set_tup)

dict_tup = dict.fromkeys(tuple_data)
print(type(dict_tup))
print(dict_tup)

# dictionary conversion

d = {1: 2, 3: 4}
print(d.items())
print(d.keys())
print(d.values())