
def lengthOfLongestSubstring(s: str) -> int:
    left_pointer = 0
    right_pointer = 0
    max_size = 0
    hash_set = set()
    while(right_pointer < len(s)):
        if (s[right_pointer] not in hash_set):
            hash_set.add(s[right_pointer])
            right_pointer += 1
            max_size = max(len(hash_set), max_size)
            print(hash_set, max_size)
        else:
            hash_set.remove(s[left_pointer])
            left_pointer += 1
        print(hash_set, max_size, 'here')
        # right_pointer += 1 never increment right pointer outside if it will cause left pointer to
        # lag behind

    return max_size

print(lengthOfLongestSubstring('abcabcbb'))