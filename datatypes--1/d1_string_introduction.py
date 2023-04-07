
s1 = "rajat"
s2 = "landge"
s3 = "what a beautiful day this"
s4 = "12-01-2022"
s5 = "rajat123456"
s6 = "12345"
#concatinating of string = i.e addition
print("concatinating string s1 =", s1+" "+s2)

# multiplication of string
print(s2*3)

# capitalise of strig = only 1st word of 1st letter is capitalise
print("capitalise of string s3 =",s3.capitalize())

# upper = all in capital
print(s3.upper())

# title = all first letter of word in string is capital
print(s3.title())

# length of string
print("length of s3 =", len(s3))

# startwith replace split joint isalnum isnumeric isalpha isdigit
print("startwith output s1=", s1.startswith('w'))
print("replace output s4=", s4.replace("-","/"))
print("split output s3=", s3.split())
print("join output s3 with '.'=", ".".join(s3))
print("isalnum of s5=", s5.isalnum())
print("isnumeric of s6=" , s6.isnumeric())
print("isalpha of s2=", s2.isalpha())
print("isdigit of s6=", s6.isdigit())

# count
rr = "i scream you scream we all scream of ice cream"
print("count of scream=", rr.count('scream'))
print("count of a=", rr.count('a'))
