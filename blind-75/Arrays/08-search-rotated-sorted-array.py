'''
https://www.youtube.com/watch?v=U8XENwh8Oy8&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=8
https://leetcode.com/problems/search-in-rotated-sorted-array/

here is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
'''
from typing import List
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid

        # Left sorted Portion
        if nums[l] < nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid -1 
            else: 
                l = mid + 1
        # Right sorted Portion
        else:
            if nums[r] >= target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
    return -1

print(search([4,5,6,7,0,1,2],0))