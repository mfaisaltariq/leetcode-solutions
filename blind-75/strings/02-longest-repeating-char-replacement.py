def characterReplacement(s: str, k: int) -> int:
    l = 0
    res = 0
    max_freq = 0
    char_count = {}

    for r, val in enumerate(s):
        char_count[val] = 1 + char_count.get(val, 0)
        max_freq = max(max_freq, char_count[val])

        while (r - l + 1) - max_freq > k:
            l += 1
            char_count[s[l]] -= 1

        res = max(res, r - l + 1)

    '''
    The below code is also valid but it increases complexity to 26 * n 
    which will still be O(n) but not that efficient as we need to find the max out of 26 chars
    worst case senario 
    '''
    # for r, val in enumerate(s):
    #     char_count[val] = 1 + char_count.get(val, 0)

    #     while (r - l + 1) - max(char_count.values()) > k:
    #         l += 1
    #         char_count[s[l]] -= 1

    #     res = max(res, r - l + 1)

    return res

print(characterReplacement('AABABBA', 1))
        