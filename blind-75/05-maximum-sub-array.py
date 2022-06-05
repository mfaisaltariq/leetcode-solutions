from typing import List
def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        
        cur_sum += n
        max_sum = max(cur_sum, max_sum)

    return max_sum





print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''