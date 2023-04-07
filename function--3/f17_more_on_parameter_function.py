# function are block of organised code that can be use repetitively.

# syntex

# def function_name(parameter1, parameter2):
    # line1
    # line2
    # line3
    #......
    # line_n

# avg = float(input("enter average"))

# if avg >= 90:
#     print("Toppers")
# elif avg >= 75:
#     print("Distinction")
# elif avg >= 60:
#     print("first class")
# elif avg >= 50:
#     print("second class")
# elif avg >= 40:
#     print("pass class")
# else:
#     print("Fail")
#
# print("------------")

def check_class():
    avg = float(input("enter average"))
    if avg >= 90:
        print("Toppers")
    elif avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("first class")
    elif avg >= 50:
        print("second class")
    elif avg >= 40:
        print("pass class")
    else:
        print("Fail")


check_class()


# check_class()
# check_class()
# check_class()
#
# print("----------")
#
# for _ in range(0,10):                                   #when variable(i,num etc) in loop not in use then _(underscore)is use.
#     check_class()

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


print(is_prime(13))
print(is_prime(73))
print(is_prime(12))

print("-------------")


# def function with arguments and rules of arguments with function.

def get_values(age, height, weight, gender, allergy):
    print("age=", age)
    print("height=", height)
    print("weight=", weight)
    print("gender=", gender)
    print("allergy=", allergy)


get_values(55, 5.9, 63, "M", "dust particle")  # this is positional arguments
print()
get_values(5.6, 66, "M", "sinus", 66)  # thus in positional arguments always maintain sequence.  disadvantages

print()
# keyword arguments
get_values(gender="M", height=6.1, age=23, allergy="lactose intolerant", weight=69)  # this is keyword arguments
print()


# default arguments
def get_values1(age, height, weight, gender, allergy, covid=False, omnicorn=False):
    print("age=", age)
    print("height=", height)
    print("weight=", weight)
    print("gender=", gender)
    print("allergy=", allergy)
    print("covid=", covid)
    print("omnicorn=", omnicorn)


get_values1(age=28, height=6.3, gender="M", weight=63, allergy="sinus")
print()
get_values1(age=28, height=6.3, gender="M", weight=63, allergy="sinus", covid="severe", omnicorn="positive")
print()
get_values(42, 6.1, 65, gender="F", allergy="dustparticle")

print("default argument example")


def calculate_interest(principal, rate=6.5):
    return (principal / 100) * rate


print(calculate_interest(5000))
print(calculate_interest(5000, 10))

# def get_values1(age, height, weight, gender, allergy, covid=False, omnicorn=False):

# rules with arguments
# get_values(23, 6.5, 69, "M")    #TypeError: get_values() missing 1 required positional argument: 'allergy'
# get_values(23, 5.9, 63, "F", "sinus", "one more value")   #TypeError: get_values() takes 5 positional arguments but 6 were given
# get_values(42, height=6.1, 65, "F", allergy="dustparticle" )  #SyntaxError: positional argument follows keyword argument
# get_values1(42, 5.3, 63)   #TypeError: get_values1() missing 2 required positional arguments: 'gender' and 'allergy'
# but does not give error for default value like covid and omnicorn.
# get_values1(23, 5.9, 63, "F", "sinus", "extra value", "one more extra", "real extra")#TypeError: get_values1() takes from 5 to 7 positional arguments but 8 were given
