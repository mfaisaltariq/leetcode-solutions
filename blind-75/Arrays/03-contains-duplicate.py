'''
https://www.youtube.com/watch?v=3OamzN90kPg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=3
https://leetcode.com/problems/contains-duplicate/
'''
from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    hast_set = set()
    for n in nums:
        if n in hast_set:
            return True
        hast_set.add(n)
    
    return False


print(containsDuplicate([1,2,3,4,6,6,7]))
print(containsDuplicate([1,2,3,4,6,7]))