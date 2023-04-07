import re                                       # re = regular expression

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

pattern =  re.compile(r"abc")
matches = pattern.finditer(text)

# for match in matches:
#     print(match.group())             # return what we find in pattern
#     print(match.span())              # give index for which we can find in pattern
#

# ------------------------------------
# finditer --- return an iterator object of the pattern matches from the provided string.
#  we iterate over it to see or extract more things

# matches = pattern.finditer(text)
# matches = pattern.finditer(text, endpos=44)
# matches = pattern.finditer(text, pos=102)
# matches = pattern.finditer(text, pos=40, endpos=120)

# for match in matches :
#
#     print(match.group())
#     print(match.span())
#     print(match.end())
#     print(match.start())
#     print(match.string)         # return sting where we find patterns.

# --------------------------------------
# findall ---- return list of match

# matches = pattern.findall(text)
# matches = pattern.findall(text, pos=40)
# matches = pattern.findall(text, endpos=112)
# matches = pattern.findall(text,pos=10, endpos=100)

# print(matches)

# --------------------------------------
#  search --- return the first match object if found else none.
#  category = uc001 to uc999

s = "UC80g- Phishing Attack"

pattern = re.compile(r"UC\d\d\w")
match = pattern.search(s)

if match:
    print("event occured")
    print(match)
else:
    print("not occured")

#
# pattern = re.compile(r"abc")
# matches = pattern.search(text)
# matches = pattern.search(text, pos=, endpos=)
# print(matches)

# --------------------------------
# split =
#
# pattern=  re.compile(r"yyyyy")
# data = pattern.split(text)
# print(data)


# matches = re.finditer(pattern, text)                 # either way for run this function--3
# matches = re.findall(pattern, text)
# matches = re.search(pattern, text)
# matches = re.split(pattern, text)