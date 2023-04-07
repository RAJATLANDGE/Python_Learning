 # *args = arbitary argument
def check_strings(name):
    if name.isdigit():
        return False
    return name.upper()

print(check_strings("amitabh"))
print(check_strings("amit"))
print(check_strings("rahul"))
print(check_strings("ranjit"))
print(check_strings("1236985"))

def check_strings2(*args):
    uppended_list = []
    for item in args:
        if item.isalpha():
            uppended_list.append(item.upper())
    return uppended_list

print(check_strings2("amitabh", "amit", "rahul", "ranjit", "99556"))


def arbitary_function(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print("-------------")

    for key, value in kwargs.items():
        print(F"{key.title()}--> {value}")

arbitary_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sum= 51, avg=25)
print()

def all_param(a, b, c, d, de = 10, *e, **f):
    print(a)
    print(b)
    print(c)
    print(d)
    print(de)
    print(e)
    print(f)

all_param(5, 8, 9, 6, 22, 51, 65, 88, 97, 15, 23, 56, 41, 51, test1= 101, test2= 102, test3= 105)
print()
all_param(5, 8, 9, 6, 22, test1= 101, test2= 102, test3= 105)
print()
# all_param(5,6,7, d=10, de=13, 22, 99, 66,33,22,11, test1= 55, test2= 96 )  #SyntaxError: positional argument follows keyword argument
#all_param(5, 6, 7, 22, 99, 66, 33, 22, 11, de=15, test1= 55, test2= 96 )  #TypeError: all_param() got multiple values for argument 'de'

def read_news(username, password, get_news, *city_filter, **date_filter):
    print(username)
    print(password)
    print(get_news)
    print(city_filter)
    print(date_filter)

read_news("USNAME", "pass123", "google_news", "pune", date= "02-02-2022")

data = ["ashish", "mahesh", "nitin", "saurabh"]

# def list_upper(data):
#     return [item.upper for item in data]
#
# print(list_upper(data))
# print(list_upper(["ashish", "mahesh", "nitin", "saurabh"]))