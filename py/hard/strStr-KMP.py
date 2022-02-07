"""
The KMP algorithm first calculates the longest prefix suffix array which enable us to keep a record of 
previously found matches and not check them again therefore reducing complexity

Example: mississippi, issip

issi occurs in the string twice so we need to keep check that the first one is not the same as last

a a a c a a a a
p i
[0,1]

a a a x a a a a
  p i
[0,1,2]

a a a x a a a a
    p i
[0,1,2]

a a a x a a a a
  p   i
[0,1,2]

a a a x a a a a
p     i
[0,1,2,0]

a a a x a a a a
p       i
[0,1,2,0,1]

a a a x a a a a
  p       i       
[0,1,2,0,1,2]

a a a x a a a a
    p       i       
[0,1,2,0,1,2,3]

a a a x a a a a
      p       i       
[0,1,2,0,1,2,3]

a a a x a a a a
    p         i       
[0,1,2,0,1,2,3,3]

Complexity for creating LPS is 2 * N where N = len of needle

"""



def strStr(haystack: str, needle: str) -> int:
    if needle == "" : return 0

    lps = [0] * len(needle)
    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[prevLPS] == needle[i]:
            lps[i] = prevLPS +1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            i += 1
        else:
            prevLPS = lps[prevLPS-1]

    i = 0 # ptr for haystack
    j = 0 # prt for needle

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j -1]
            
        if j == len(needle):
            return i - j
    
    return -1

print(strStr("aaacaaaa", "aaaa"))
print(strStr("mississippi", "issip"))