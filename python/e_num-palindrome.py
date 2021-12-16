'''
// Given an integer x, return true if x is palindrome integer.

// An integer is a palindrome when it reads the same backward as forward.

// For example, 121 is a palindrome while 123 is not.
'''

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0 or x < 10:
        return True
    num_str = str(x)
    num_len = len(num_str)
    for i in range(int(num_len/2)):
        if num_str[i] != num_str[-(i+1)]:
            return False
    return True

print(isPalindrome(-121))