
# * right angle tringle pattern
def first_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print( )

print("first pattern")
first_pattern(5)

# shortcut right angle tringle pattern
def shortcut_first_pattern(n):
    for i in range(1, n+1):
        print("* " * i)

print("shortcut first pattern")
shortcut_first_pattern(5)

# triangle pattern (tree without stream)
def second_pattern(n):
    for i in range(0, n):                             # for line
        n -= 1
        for j in range(0, n):                        # for space
            print(end = " ")
        for k in range(0, i+1):                      # for star
            print("*", end = " ")
        print()

print("second pattern")
second_pattern(5)

def shortcut_second_pattern(n):
    for i in range(0, n+1):
        print(" "*n + "* "*i)
        n -= 1

print("shortcut second pattern")
shortcut_second_pattern(5)

# reverse of 1st pattern
def third_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print("* ", end="")
        print()

print("third pattern")
third_pattern(5)

def shorcut_third_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

print("shortcut third pattern")
shorcut_third_pattern(5)


def fourth_pattern(n):
    for i in range(0, n):
        n -= 1
        for j in range(0, i+1):
            print(end= " ")
        for k in range(n+1, 0, -1):
            print("*", end= " ")
        print()

print("fourth pattern")
fourth_pattern(5)

def shortcut_fourth_pattern(n):
    for i in range(1, n+1):
        n -= 1
        print(" "*i + "* "*(n+1))

print("shortcut fourth pattern")
shortcut_fourth_pattern(5)


# def x-mas_tree(n):
