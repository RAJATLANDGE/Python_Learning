# user define function
# sylntax

# defining
# def function_name():
    #first line
    #second line
    #.
    #.
    #.
    # nth line
#any line

# calling
# function_name()
print("before function def")

def even_or_odd():
    print("entered function currently on line1")
    print("Inside function on first line")
    for num in range(1,11):
        if num%2==0:
            print(f"{num} is Even")
        else:
            print(f"{num} is odd")
    print("Exiting function on last second line")
    print("printing last line of function")

print("after function def")

even_or_odd()        #this is called calling the function. after this calling the
                     # function is execute otherwise not execute in output bar.

print("-----------------------------------")

