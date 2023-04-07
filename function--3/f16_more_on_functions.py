
def non_parameterized_function_and_returns_none():
    return None
    pass
def non_parameterized_function_and_returns_something():
    return something #(eg string, number, boolean etc)
    pass
# e.g  below

print("non_parameterized_function_and_returns_something example")
print("test")

# return does not execute if statement is false i.e does not give output in console
def is_even():
    if 98%2==0:
        return True
    else:
        return False

is_even()
print(is_even())

if is_even():
    print("even")

result = is_even()

if result:
    print("second even")
else:
    print("odd")

print("--------------")

def parameterized_function_and_returns_none():
    return None

def parameterized_function_and_returns_something():
    return      #"welcome(i.e anything string, number, boolan.....")
    pass


def is_even_none(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

is_even_none(48)
is_even_none(49)
is_even_none(98)
is_even_none(99)
is_even_none(78)
is_even_none(73)

print("---------")
def is_even_something(num):
    if num%2==0:
        return True
    else:
        return False

print(is_even_something(89))
print(is_even_something(99))
print(is_even_something(52396545223))
print(is_even_something(88520696238))

