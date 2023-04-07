# write the function to remove the duplicate from list

sample_data = [2,5,9,8,7,6,3,2,5,8,4,1,3,9,5,6,8,4,7,5,2,3,6,9,2,1,4,5,6,56,39,89,2,3,6,8,5,2,1,4,9,6,3,]

def remove_duplicates(data):
    data = set(data)
    return list(data)

print("remove duplicate using inbuild function =", remove_duplicates(sample_data))

# write the function to remove the duplicate from list without using inbuild function

def remove_duplicates_noninbuilt(data):
    non_duplicate_list = []
    for item in data:
        if item not in non_duplicate_list:
            non_duplicate_list.append(item)
    return non_duplicate_list

print("remove duplicate without using inbuild function--3 =", remove_duplicates_noninbuilt(sample_data))

# write the function to remove the duplicate from list without using inbuild function and without using a new list/datatype

def remove_inbuild_without_inbuilt_and_without_using_newlist(data):
    for item in data:
        if data.count(item) == 2:
            data.remove(item)
    for index, item in enumerate(data, 0):
        element_count = data.count(item)
        if element_count >1 and element_count != 2:
            for _ in range(0, element_count-1):
                data.remove(item)
    return data

print("without inbuilt and without new list =",remove_inbuild_without_inbuilt_and_without_using_newlist(sample_data))

# write a function that a takes a string of parenthesis and tells whether given string balance or not.
class InvalidInput(Exception):
    pass

def is_balanced(input_string):
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = []
    open_brackets = list(brackets.keys())
    closed_brackets = list(brackets.values())

    for char in input_string:
        if char not in open_brackets and char not in closed_brackets:
            raise InvalidInput("Given input is not valid parenthesis")

    for bracket in input_string:
        if bracket in open_brackets:
            stack.append(bracket)

        if bracket in closed_brackets:
            last_open_bracket_read = stack.pop()
            index = closed_brackets.index(bracket)
            match_open_bracket_to_close_bracket = open_brackets[index]

            if match_open_bracket_to_close_bracket != last_open_bracket_read:
                return False

    if len(stack) != 0:
        return False

    return True

print(is_balanced("({[]})"))
print(is_balanced("[(({({[]}))})]"))

# write a program to print smallest and largest number from given list.

data = [475, 526998, 256639, 8875456, 253, 23, 56, 2478935, 4269836, 2588741213955, 56, 78, 63, 95, 82, 99]
print("max number =",max(data))
print("min number =",min(data))

# without using inbuild function--3
smallest = data[0]
largest = data[0]
for elm in data:
    if elm > largest:
        largest = elm

    if elm < smallest:
        smallest = elm

print("smallest", smallest)
print("largest", largest)
