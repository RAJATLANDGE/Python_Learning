# nested function=  that is function under function and popularly use in decorators defining.
# syntax
def outer_function():
    print("Enter insider outer")
    def inner_function():
        print("inside inner")
        print("executing lines in inner")
        print("exiting inner")
    inner_function()
    print("exiting outer")
outer_function()

print()

# recursive function = a function that call it self is called recursive function. recursive function max limit 1000 times.
fact5 = 5*4*3*2*1

def factorial_funtion(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i        # this line means = fact * i
    return fact

print(factorial_funtion(5))

# same above factorial function in recursive function.
def fact(n):
    if n==1:
        return 1
    else:
        return n* fact(n-1)

print(fact(6))