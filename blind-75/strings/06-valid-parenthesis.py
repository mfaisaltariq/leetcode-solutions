def isValid( s: str) -> bool:
    my_stack = []

    for char in s:
        if char is '(' or char is '{' or char is '[':
            my_stack.append(char)
            continue
        else:
            if not my_stack:
                return False

            last_pop = my_stack.pop()
            if last_pop is '(' and char is not ')' : return False
            if last_pop is '{' and char is not '}' : return False
            if last_pop is '[' and char is not ']' : return False

    if my_stack:
        return False
    else:
        return True

def isValid2( s: str) -> bool:
    stack = []
    close_to_open = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
                continue
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False
        

print(isValid("()[]{}"))
print(isValid2("()[]{}"))