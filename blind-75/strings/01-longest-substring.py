def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    res = 0
    char_set = set()

    for r, val in enumerate(s):
        while val in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(val)
        res = max(res, r - l + 1)

    return res

print(lengthOfLongestSubstring('pwwkew'))