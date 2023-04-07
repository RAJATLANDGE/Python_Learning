# any function with yield statement is called generator function.
# for read generator function we use next() function.


def function1():
    yield 1
    yield 2
    yield 3
    yield 4

gen_obj1= function1()

print(next(gen_obj1))
print(next(gen_obj1))
print(next(gen_obj1))
print(next(gen_obj1))
# print(next(gen_obj1))
try:
    print(next(gen_obj1))
except StopIteration:
    pass


print("------------------")

def num_generator(n):
    for i in range(1,n+1):
        yield i

obj_num = num_generator(10)
for num in obj_num:
    print(num)

print("------------------")



student_marks = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]


def marks_generator():
    for marks in student_marks:
        yield marks

# print(marks_generator())               # give generator object -><generator object marks_generator at 0x000001C006CFDDC8>

gen_obj2 = marks_generator()

print(next(gen_obj2))
print(next(gen_obj2))
print(next(gen_obj2))
(next(gen_obj2))              # if we did not use this value then it does not show it, ie print it
print(next(gen_obj2))

for item in gen_obj2:
    print(item)

def gen_100():
    for item in range(1,100):
        yield item

gen_obj3 = gen_100()

for i, item in enumerate(gen_obj3,1):
    if item > 5:
        print(f"{i}--> {item}")

def gen_10():
    for item in range(1,11):
        yield item

gen_obj4 = gen_10()

n = 5
for i in range(1,n):
    next(gen_obj4)

for i in range(6,11):
    print(next(gen_obj4))














