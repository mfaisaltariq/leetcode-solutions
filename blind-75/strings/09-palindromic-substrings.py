
def countSubstrings(s: str) -> int:
    counter = len(s)
    
    for i in range(len(s)):
        l, r = i, i
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l +1) > 1:
                counter += 1
                
            r += 1
            l -= 1
        
        l, r = i, i + 1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l +1) > 1:
                counter += 1
                
            r += 1
            l -= 1
    return counter
    
print(countSubstrings("aaa"))