def strStr(haystack: str, needle: str) -> int:
    substring_len = len(needle)
    if substring_len == 0:
        return 0
    if len(haystack) == 0:
        return -1
    if needle in haystack:
        return len(haystack.split(needle)[0])
    else:
        return -1

    #### below solution doesn't work for last test case so had to use internal functions
    # substring_len = len(needle)
    # if substring_len == 0:
    #     return 0
    # if len(haystack) == 0:
    #     return -1
    # # if substring_len == 1:
    # #     return haystack.index(needle)
    # pointer = 0
    # index = 0
    # substring_len = len(needle)
    # for char in haystack:
    #     print(pointer, substring_len, index, 'here1')
    #     if char is needle[pointer]:
    #         print(pointer, substring_len, index, 'here3')
    #         pointer +=1
    #     else:
    #         pointer = 0
        
    #     index +=1
    #     if pointer == substring_len:
    #         print(pointer, substring_len, index, 'here')
    #         break
    #         # return index - pointer

    # print(pointer, substring_len, index, 'here4')
    # if pointer < substring_len:
    #     return -1
    # else:
    #     return index - pointer

print(strStr('a', 'a'))
print(strStr('a', ''))
print(strStr('', ''))
print(strStr('', 'a'))
print(strStr('hello', 'll'))
print(strStr('bbb', 'bbb'))
print(strStr("mississippi","issip"))