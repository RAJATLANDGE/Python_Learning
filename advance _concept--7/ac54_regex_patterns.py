import re

# ip address range of numbere 0 to 255
text = '''
abcjojreptjptwoperpoowkerp
ABCJLKJREOITJOIRJTRJOIJRII
lkfj
yyyyy
ljfjk
jkfp
krpok
yyyyy
kjrepk

lkpgkre
fgklk
yyyyy
oigjerpk
abc
pqr
lmn
yyyyy
xyz
123.256.238.23
125.789.23.2
yyyyy
12.369.2.8

'''
# regex = regular expression
# Meta Characters


# \d      - Digit (0-9) - searches for numbers 0-9 in the string
# \D      - searches for anything except number -

# pattern = re.compile(r"\d")
pattern = re.compile(r"\d\d\d")
# pattern = re.compile(r"\d\d.\d\d.\d\d")                     # .(dot)= any character (0-9, a-b, A-B, symbol etc)
# pattern = re.compile(r"\d\d\.\d\d\.\d\d")                   # \. = specific dot
# pattern = re.compile(r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d")
# pattern = re.compile(r"\d\d\.\d\.\d\d\d\.\d\d")
#
# pattern = re.compile(r"\D")
# pattern = re.compile(r"\d\d\d.\D\D\D.\d\d\d\d")

print(pattern.findall(text))

#\w   -  Word charcter alphabet (a-z, A-Z,0-9, _)
#\W   - Not a word charcter

# pattern = re.compile(r"\w")
# pattern = re.compile(r"\W")
pattern = re.compile(r"\w\w\w\w")
# pattern = re.compile(r"\w+@\w+\.\w+")        ## + = 1 or more
# pattern = re.compile(r"\w+\W\w\W\w+")
# pattern = re.compile(r"\w+\W\w+\W\w+")

print(pattern.findall(text))

# for ip adress
# pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")



# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
pattern = re.compile(r"\s")
match = pattern.findall(text)
print(match)


# ---->    * o or more
pattern = re.compile(r"M\w*")
match = pattern.findall(text)
print(match)

# + 1 or more
pattern = re.compile(r"Mr\w+")
match = pattern.findall(text)
print(match)


# ?  zero or 1

pattern = re.compile(r"Mr\w?")
match = pattern.findall(text)
print(match)


# # {num} , exact number
pattern = re.compile(r"\d{3}.\w{3}.\d{4}")
match = pattern.findall(text)
print(match)


# {n1,n2} number range separated by comma
pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,4}")
# pattern = re.compile(r"172\.\d{2}\.\d{1,3}\.\d{1,3}")
match = pattern.findall(text)
print(match)

# [] Matches Characters in brackets,  [^] matches charcters not in brackets

pattern = re.compile(r"BBB[hijklm]\d+")  # aaa   abb abc baa bab
# pattern = re.compile(r"BBB[^hijklm]\d+")    # next to BBB other than hijklm
match = pattern.findall(text)
print(match)



# |   either/or

x = "there is no gain without pain"

pattern = re.compile(r"gain|pain")

match = pattern.findall(x)
print(match)

pattern = re.compile(r"\d\d\+\d\d\+\d\d|\d\d\*\d\d\*\d{1,4}")
match = pattern.findall(text)
print(match)
