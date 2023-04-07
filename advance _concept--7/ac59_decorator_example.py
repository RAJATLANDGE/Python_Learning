from functools import wraps
import time

def outer_function(func):

    @wraps(func)
    def inner_function(*args, **kwargs):
        print("***************************")
        #
        #
        #
        #
        func(*args, **kwargs)
        print("***************************")
        #
        #
        #
    return inner_function

@outer_function
def func_odd(n):
    if n%2!=0:
        print(f"{n} is odd ")
    else:
        print(f"{n} is even")


func_odd(27)
func_odd(13)
func_odd(12)



def timer(func):
    @wraps(func)                     # wraps help in print docstring in pass function--3 ie maintain documentation
    def inner(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        # if result:
        #     print("Balanced")
        # else:
        #     print("Not Balanced")

        t2 = time.time()
        print(f"function execution took {t2 - t1} second")
    return inner

@timer
def func_odd(n):
    if n%2!=0:
        time.sleep(5)
        print(f"{n} is odd ")

func_odd(25)

@timer
def is_balanced(input_string : str):                                           #typehints : str, list, int,.....   etc
    """
    check whether a string of parenthesis are is a balance string or not.
    uses stack for execution.
    :param input_string (str): string of parenthesis
    :return: returns true if parenthesis is balanced
    """
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = []
    open_brackets = list(brackets.keys())
    closed_brackets = list(brackets.values())
    time.sleep(4)

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

is_balanced("({[})")


# def admin_only(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print(args[0])
#         user = oneUser.objects.get(username = args[0].user)
#         if user.role == "admin"
#             a = func(*args, **kwargs)
#         return  a
#         else:
#             return HttpResponse ("you are not admin")
#     return inner












