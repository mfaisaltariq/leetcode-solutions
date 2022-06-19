'''
This is a Hard Problem
https://www.youtube.com/watch?v=jSto0O4AJbM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=51
'''
def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
        
    countT, window = {}, {}
    for char in t:
        countT[char] = 1 + countT.get(char, 0) 
    
    have, need = 0, len(countT)
    res, resLen = "", len(s) + 1
    l = 0
    for r,val in enumerate(s):
    
        if val in countT:
            window[val] = 1 + window.get(val, 0)
            if window[val] == countT[val]:
                have += 1
    
        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = s[l:r+1]
                resLen = (r - l + 1)
            
            if s[l] in countT:
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
            l += 1
    return res if resLen != len(s) + 1 else ""

print(minWindow('A', 'AA'))        
