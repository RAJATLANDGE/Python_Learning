# defining dictionary
# empty_new_dictionary = {}
# empty_new_dictionary = dict()
# data_dictionary = {'key1': 'element', 'key2': 'element2', 'key3': 'element3',......'keyn': 'elementn'}

# introdution
my_prefrence = {"fruit": "apple", "food": "indian", "country": "india", "colour": "white"}

indian_team = {"captain": "Dhoni", "vc": "Rahane", "batsmen": ["rohit", "balaji", "Robin"], "wk": "Pant",
               "bowlers": {"spin": ["Jasprit", "Ashwin", "Jadeja"], "fast": ["Ishant", "Shami"]}, "coach": "Rahul D"}

print(my_prefrence)
print(indian_team)

# Reading dictionary ---
#   1)# in below operation get error if passed element is not present.

print(indian_team['captain'])
print(indian_team['bowlers']['spin'][2])
print(indian_team['coach'])

#   2) dictionary.get('key', '<default_value>') ----- reads the key, if key present in dictionary it will return vaule of that
# if key is not present it will return default value. if default value is not specified it will return none.

print(indian_team.get('vc'))
print(indian_team.get('physio'))
print(indian_team.get('physio','ramgopal'))    # if key not given then give default value.
print(indian_team.get('all_rounder', ['hardik', 'klrahul']))

#  items() , keys(), values()
print("dictionary items", indian_team.items())
print("dictionary keys", indian_team.keys())
print("bowlers keys", indian_team['bowlers'].keys())   # bowlers value is in dictionary so dictionary function--3 is use
print("dictionary value", indian_team.values())
print(indian_team['batsmen'][1])        # batsmen value is in list so list funtion is use

# dictionary.update(<new-_dictionary)-------update the dictionary with passed dictionary

indian_u19 = {"u19": {"captain": "piyush", "vc": "akash"}}
medium = {'medium': ["shardul", "sundar"]}

print("before update", indian_team)
indian_team.update({"12thman": "yusuf", "runner": ["ganguly", "gavaskar"]})   # update key and value always in dictionary
                                                                              # i.e in {}because it add dictionary in dictionary
indian_team.update(indian_u19)
print("after update", indian_team)

indian_team['bowlers'].update(medium)
print(indian_team['bowlers'])

# setdefault(key, default_vaule)    ---
# 1) if key is present returns the value of key .
# 2) if key is not present returns the default value and update the dictionary with key and provided default value as is value.
def_date = indian_team.setdefault("captain", "siddhu")              # when key is already present in dictionary
print("first senario", def_date)
def_data2 = indian_team.setdefault("sponser", "TATA")        # when key is not present in dictionary
print("second senario", def_data2)
print("final dictionary", indian_team)

#  dict().fromkeys(<list>, default_value)  ---
#  1)can be used to creat dictionary from list
#  2)it take the list and it will creat the dictionary keys will be element present in the list and value of those keys
#      default value if provided if default value is not provided value will be none.
my_pref = ["fruit", "sport", "cuisine", "colors"]
weather = ["temp", "windspeed", "unit", "location"]

temp_data = dict().fromkeys(weather)
new_data = dict().fromkeys(my_pref, "unknown")
print("weather dict=", temp_data )
print("newly created data", new_data)

temp_data["temp"] = "40 C"
temp_data["windspeed"] = "55  km/h"
temp_data["unit"] = "degree celcius"
temp_data["location"] = "Nagpur"
print("weather dict=", temp_data )
print("before pop", indian_team)
# pop and popitem
indian_team.pop("captain")
indian_team.popitem()        # remove one of the item in given dictionary
print("after pop", indian_team)

# copy
indian_u25 = indian_team.copy()
print("copied under_u25", indian_u25)

# clear
indian_team["bowlers"].clear()
print("remove of bowlers=", indian_team)
indian_team.clear()
print("clear dictionary=", indian_team)