"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

SOLUTION:
We have to find the highest common prefix in a given array of string so that means we just need to check
the least common elements of the array. We can sort the array and then check only first and last element
to find the largest common prefix.

complexity is log o(n) * min(range)
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    sorted_list = sorted(strs)
    longest_prefix = ""
    for i, j in zip(sorted_list[0], sorted_list[-1]):
        if i is j:
            longest_prefix += i
        else:
            return longest_prefix

    return longest_prefix

print(longestCommonPrefix(["flow","flow","flowht"]))
print(longestCommonPrefix(["dog","racecar","car"]))