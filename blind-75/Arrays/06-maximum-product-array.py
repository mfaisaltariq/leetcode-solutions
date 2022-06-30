'''
https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''
from typing import List
def maxProduct(nums: List[int]) -> int:
    max_product = max(nums)
    curr_min, curr_max = 1,1

    for n in nums:
        if n == 0:
            curr_min, curr_max = 1,1
            continue

        tmp = curr_max * n
        curr_max = max(curr_max * n, curr_min * n, n)
        curr_min = min(tmp, curr_min * n, n)
        max_product = max(max_product, curr_max)

    return max_product

print(maxProduct([2,3,-2,4]))
print(maxProduct([-1,-2,-3]))
