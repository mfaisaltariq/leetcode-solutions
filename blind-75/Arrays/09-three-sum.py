'''
https://www.youtube.com/watch?v=jzZsG8n2R9A&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=9
https://leetcode.com/problems/3sum/
'''
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, val in enumerate(nums):
        if i > 0 and val == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1 
        while l < r:
            three_sum = val + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0: 
                l += 1
            else:
                res.append([val , nums[l] , nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-2,-2,0,0,2,2]))

