
days = ["mon", "tues", "wed","thus", "fri", "sat", "sun"]
numbers = [1,2,3,4,5,6,7,8,9,10]
months = ["jan", "feb", "march", "april", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]

for index,day in enumerate (days,0):
    print(f"{day} --> {numbers[index]}")

print("--------------------")

zip_data = zip(days,numbers,months)                           #pick shortest list # zip give generator object
                                                              #zip, zip the 2 or more list
for day,num,mon in zip_data:
    print(f"{day}-> {num}-> {mon}")

print("-----------------")

# ziplongest

from itertools import zip_longest
zip_long = zip_longest(days, numbers, months, fillvalue="%%%")

for day, num, mon in zip_long:
    print(f"{day} -> {num} -> {mon}")



#filter - did not save none, true, false, only save required output

alpha_numeric = ["jfgoerjo4","orj094lo","ol40904","ldfpp4e/34","krp-dfe3"]

filtered_data = list(filter(str.isalnum,alpha_numeric))      #(function,object)     #give generator type object hence use list
print(filtered_data)

number = [2365,669542,256958,23,69,58239,2341,266985,336699,225847]

def is_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

prime_numbers = list(filter(is_prime,number))
print(prime_numbers)


# map - save anthing ie true false string integer etc and give output       # it also return generator function hence use list

def capital_string(name):
    title_list = []
    name_list = name.split()     # ["sachin", "tendulkar"]
    for item in name_list:
        nm = item[0].upper() + item[1:]
        title_list.append(nm)
    capital_string = " ".join(title_list)
    return capital_string


names = ["saurabh ganguly","kapil dev","brian lara","glenn mcGrath"]

map_output = list(map(capital_string,names))
print(map_output)




areas = [5582.36982,3658.23695,2369.36942,1452.3982,1987.3654]
pt = [2]*len(areas)
# pt = [1,2,3,4]

map_areas = list(map(round,areas,pt))
print(map_areas)


# a = {23:56, 44:89, 25:}
# print([2]*len(areas))