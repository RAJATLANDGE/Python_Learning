# string assignment
# reverse of string

# 1) using slicing
s1 = "string assignment"
print("by using slicing =", s1[::-1])

# 2) using for-loop
s2 = ""
for c in s1:
    s2 = c + s2
print("by using for-loop =", s2)

# 3) using reverse
print("by using reverse=", "".join(reversed(s2)))

# 4)using recursion
def string_rev(s):
    if len(s)==0:
        return s
    else:
        return string_rev(s[1:]) + s[0]

print("by using recursion=", string_rev("pots"))

# string_rev(pots)= string_rev(s[1:]) + s[0] = string_rev(ots) + p ----> sto+p
# string_rev(ots)= string_rev(s[1:]) + s[0] = string_rev(ts) + o   ---->st+o
# string_rev(ts)= string_rev(s[1:]) + s[0] = string_rev(s) + t     ---->s+t
# string_rev(s)= string_rev(s[1:]) + s[0] = string_rev("") + s     ---->""+s
# string_rev("")= return s = return ("")= empty

# write a function that check whether a given string is palindrome or not.
def is_pallindrome(s1):
    s2 = s1[::-1]
    if s1 == s2:
        return True
    else:
        return False

print("---->",is_pallindrome("madam"))

# or
def is_pallindrome(s1):
    return s1 == s1[::-1]
print("---->",is_pallindrome("radar"))

# write a function to check whether two string are anagram to each other or not.
def are_anagram(first, second):
    if len(first) != len(second):
        return False

    sorted_first = sorted(first.lower())
    sorted_second = sorted(second.lower())
    if sorted_second == sorted_first:
        return True
    return False

print("anagram check=", are_anagram("heart", "earth"))
print("anagram check=", are_anagram("hearT", "Earth"))

first = "A decimal point"
second = "im a dot in place"

def are_a_anagram(first, second):
    # if len(first) != len(second):
    #     return False
    first_replace = first.replace(" ", "")
    second_replace = second.replace(" ", "")
    first_lower = first_replace.lower()
    second_lower = second_replace.lower()
    first_sorted = sorted(first_lower)
    second_sorted = sorted(second_lower)

    if first_sorted == second_sorted:
        return True
    return False
    # for ch in first_sorted:
    #     if ch not in second_sorted:
    #         return False
    # return True

print(are_a_anagram("first_sorted", "second_sorted"))