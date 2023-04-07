# 1) write the program to calculate sum of digit of the number
# 2) write the function that takes a number as input and returns the sum of its digit.

num = 12345
sum = 0

#  1)
while num > 0:
    sum += num % 10                              # % give remainder (modulo)
    num = num // 10                              #give divisior without point (floor division)
print(sum)

# 2)
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10

    return sum
print(sum_of_digits(12345))

# write the function that accept a number and tells whether it is armstrong number or not

def is_armstrong(num):      #armstrong -> original number = sum of cube of each digit

    original_num = num
    cube_sum = 0
    while num > 0:
        digit = num%10
        cube_sum += digit**3
        num = num//10      #(or num//=10)
    if original_num == cube_sum:
        print(f"{original_num} is armstrong number")
    else:
        print(f"{original_num} is not armstrong number")

is_armstrong(407)
is_armstrong(236985478)


# HW
# 1) write the program that revers the number.
# 2) write the function that return the number in reverse.

# 1)
num = 12345
reversed_no = 0
while num>0:
    digit = num % 10
    reversed_no = reversed_no * 10 + digit
    num = num//10
print(reversed_no)

# 2)
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num
print(reverse_number(123456))

# 3) is_even
def is_even(num):
    while num%2==0:
        return ("even")
    else:
        return ("odd")

print(is_even(8698))

# 4) is_odd
num = 893
if num%2==1:
    print("odd")
    # break
else:
    print("even")

# 5) is_prime
num = 23
for i in range(2, num):
    if num%i == 0:
        print("not prime")
        break
else:
    print("prime")

# 6) in another way
def is_prime(num):
    if num == 1:
        return False

    num_list = list(range(2, num))
    prime = True
    for div in num_list:
        if num%div==0:
            prime = False
            break 

    if prime:
        print("number is prime")
    else:
        print("number is not prime")


# in another way

def is_prime(num):
    if num == 1:
        return False

    prime = True
    for div in range(2, (num//2)+1):
        if num%div==0:
            prime = False
            break

    if prime:
        print("number is prime")
    else:
        print("number is not prime")


# in another way
def is_prime(num):
    if num == 1:
        return False

    for div in range(2, (num//2)+1):
        if num % div == 0:
            return False
    else:
        return True

# write a programm that displays first 23 armstrong numbere
# write a program that displays all the armstrong number less than a given number

armstrong_nos =[]
def is_armstrong2():
    for num in range(1,10001):
        original_num = num
        cube_sum = 0
        while num > 0:
            digit = num % 10
            cube_sum += digit ** len(str(original_num))
            num = num // 10  # (or num//=10)
            if original_num == cube_sum:
                armstrong_nos.append(original_num)
    return armstrong_nos

print("list of armstrong number",is_armstrong2())
print()


# write a programm to check that the input pair of numbers is amicable.
# amicable numbers are found in pair. A given pair of numbers is amicable if the sum of the proper divisors
# (not including itself) of one number is equal to the other number and vice-versa.
# eg. 220 and 284 are amicable numbers
# first we find the proper divisors of 220
# 220: 1+2+4+5+10+11+20+22+44+55+110 =284
#  284: 1+2+4+71+142 = 220
# The first ten amicable pairs are: (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856),
#                                    (12285, 14595), (17296, 18416), (63020, 76084), and (66928, 66992).

def is_amicable(num1,num2):
    sum1 = 0
    sum2 = 0
    for i in range(1, num1 + 1):
        if (num1 % i == 0):
            sum1 += i

    for j in range(1,num2+1):
        if (num2 % j ==0):
            sum2 += j

    if sum1 == sum2:
        print(f"{num1} and {num2} are amicable pair")
    else:
        print(f"{num1} and {num2} is not a amicable pair")



is_amicable(220,284)
is_amicable(220,285)
is_amicable(12285,14595)
is_amicable(12285,14585)