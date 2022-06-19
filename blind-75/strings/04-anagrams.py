''' 
Easy Quetsion
https://www.youtube.com/watch?v=9UtInBqnCgA
'''

from operator import truediv


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i, val in enumerate(s):
        countS[val] = 1 + countS.get(val, 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for val in countT:
        if countT[val] != countS.get(val, 0):
            return False
    
    return True
    ''' O(S+T), space is also O(S+T)'''

print(isAnagram('tar', 'rat'))