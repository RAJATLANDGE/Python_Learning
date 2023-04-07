# write a program to reverse the sentence.

sentence = "Process finished with exit code"
sentence = sentence.split()
print(sentence)
sentence = sentence[::-1]
print(sentence)
print(" ".join(sentence))

print("------")
# or
word_list = []
word = ""
for char in sentence:
    if char != " ":
        word += char
    else:
        word_list.append(word)
        word = ""

for word in word[::-1]:
    sentence += word


# count number of vowels and consonants in a string

vovels = "aeiou"
count_vov = 0
count_cons = 0
user_input = input("Enter something with out space")
for alpha in user_input.lower():
    if alpha in vovels:
        count_vov += 1
    else:
        count_cons += 1
print("vov count", count_vov)
print("conc count", count_cons)

# for alpha in user_input:
#     if alpha not in vovels:
#         count_cons += 1
#     else:
#         count_vov += 1


'''write a function--3 that takes input and display output as below.
saurabh ganguly  ---> Saurabh Ganguly
kapil dev        ---> Kapil Dev
brian lara       ---> Brian Lara
glenn mcGrath    ---> Glenn McGrath
'''

# input_user = input("write something")
def capital_string(name):
    title_list = []
    name_list = name.split()     # ["sachin", "tendulkar"]
    for item in name_list:
        nm = item[0].upper() + item[1:]
        title_list.append(nm)
    capital_string = " ".join(title_list)
    return capital_string

print(capital_string("saurabh ganguly"))
print(capital_string("kapil dev"))
print(capital_string("brian lara"))
print(capital_string("glenn mcGrath"))