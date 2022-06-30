'''
https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=4
https://leetcode.com/problems/product-of-array-except-self/
'''
from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums)-1,-1,-1):
        result[j] *= postfix
        postfix *= nums[j]
                                     
    return result


print(productExceptSelf([1,2,3,4]))

