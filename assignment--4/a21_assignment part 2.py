# write the program that takes numbers from user in comma separated form and print the sum of total number.
# input output always in string.
numbers = input("Enter number separated using comma")
print(numbers)
numbers_list = numbers.split(",")
print(numbers_list)
sum = 0
for num in numbers_list:
    sum += int(num)

print(sum)

# write the program that takes two number from user as a range and display the list of number from that range
# where all digit or a particular number are even digits

start = int(input("inter a start range"))
end = int(input("inter a end range"))
even_list = []


for num in range(start, end+1):
    original_num = num
    while num>0:
        digit = num % 10
        if digit%2 != 0:
            break
        num //= 10
    else:
        even_list.append(original_num)

print(even_list)


emails = {"rj@gmail.com":"123"}

email = input("enter email")

if email in emails:
    password = input("enter password")
    if password == emails[email]:            #or if password == emails.get("rj@gmail.com")
        print("login success")
    else:
        print("wrong password")
else:
    print("not registered")