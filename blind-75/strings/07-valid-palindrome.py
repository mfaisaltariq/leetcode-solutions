def isPalindrome( s: str) -> bool:

    l, r = 0, len(s) -1

    while l < r:
        is_r_alphanum = isAlphaNum(s[r].lower())
        is_l_alphanum = isAlphaNum(s[l].lower())
        if not is_r_alphanum:
            r -= 1
            continue
        elif not is_l_alphanum:
            l += 1
            continue
        elif s[r].lower() != s[l].lower():
            return False
        l += 1
        r -= 1
            

    return True

def isAlphaNum(char: str) -> bool:
    return (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9') )

print(isPalindrome("A man, a plan, a cbnal: Panama"))