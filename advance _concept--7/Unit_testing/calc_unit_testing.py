
class OutputWillBeZero(Exception):
    pass

def addtion(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    if a==0 or b==0:
        raise OutputWillBeZero("one or both the argument is zero hence result will be zero, which of no use")
    return a*b

def division(a,b):
    if b==0:
        raise ZeroDivisionError
    return a/b



class InvalidInput(Exception):
    pass

def is_balanced(input_string):
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = []
    open_brackets = list(brackets.keys())
    closed_brackets = list(brackets.values())

    for char in input_string:
        if char not in open_brackets and char not in closed_brackets:
            raise InvalidInput("Given input is not valid parenthesis")

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
