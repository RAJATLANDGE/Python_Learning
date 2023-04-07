import for_import


@for_import.timer
def is_balanced(input_string):
    brackets = {"(": ")", "{": "}", "[": "]"}
    stack = []
    open_brackets = list(brackets.keys())
    closed_brackets = list(brackets.values())

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

print(is_balanced("(){}{}[][]"))
