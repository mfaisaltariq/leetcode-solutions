"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid( s: str) -> bool:
    stack = []

    for char in s:
        if char is '(' or char is '{' or char is '[':
            stack.append(char)
            continue
        else:
            if not stack:
                return False

        last_pop = stack.pop()
        if last_pop is '(' and char is not ')' : return False
        elif last_pop is '{' and char is not '}' : return False
        elif last_pop is '[' and char is not ']' : return False

    if stack:
        return False
    else:
        return True

print(isValid("()[]{})"))