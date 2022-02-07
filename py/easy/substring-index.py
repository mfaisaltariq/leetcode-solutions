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

# from typing import List
# def strStr(haystack: str, needle: str) -> int:
    # ref_arr = [0] * len(needle)
    # i, j = 1, 0
    # while i < len(needle):
    #     print(ref_arr,i, j)
    #     print(needle[i], needle[j])
    #     if needle[i] == needle[j]:
    #         j += 1
    #         ref_arr[i] = j
    #         i += 1
    #     elif j > 0:
    #         j = ref_arr[j-1]
    #     else:
    #         print('here')
    #         ref_arr[i] = 0
    #         i += 1

    # print(ref_arr)
    # return 0

# print(strStr('a', 'a'))
# print(strStr('a', ''))
# print(strStr('', ''))
# print(strStr('', 'a'))
# print(strStr('hello', 'll'))
# print(strStr('bbb', 'bbb'))
print(strStr("mississippi","issip"))
print(strStr("abcxabcdabcdabcy","aabaabaaa"))
# a a b a a b a a a
# 0 1 2 3 4 5 6 7 8