# tupple element is always constant, addition and removal of element is not happening
# e.g weeekdays = ('monday', 'tuesday', 'wednesday', 'thusday', 'friday', 'saturday', 'sunday')
#      vowel = tuple(['a', 'e', 'i', 'o', 'u'])

# define tuple
# tup1 = (<element>, <element>, <element>, <element>, <element>)
# tup2 = tuple([<element>, <element>, <element>, <element>, <element>])
# empty_tuple = ()

# --------------
months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'july', 'aug', 'sept', 'oct', 'nov', 'dec')
vowel = tuple(['a', 'e', 'i', 'o', 'u'])

print(months)
print(vowel)
print("element at index 0 =", months[0])
print("element at index -1 =", vowel[-1])

print("count of jan =", months.count('jan'))
print("index of o =", vowel.index('o'))