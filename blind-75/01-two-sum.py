'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

from typing import List

### VVI test case [3,3] with target 6 is an edge case keep it in the mind


def twoSum(nums: List[int], target: int) -> List[int]:
    my_map = {}
    result = []
    i = 0
    for i in range(len(nums)) :
        if nums[i] in my_map:
            result.append(nums.index(target-nums[i]))
            result.append(i)
            return result
        else:
            my_map[target - nums[i]] = nums[i]
    return result

print(twoSum([3,3], 6))

'''
from typing import List
## Edge Case https://leetcode.com/submissions/detail/649939365/

def twoSum(numbers: List[int], target: int) -> List[int]:
        map_num = {}
        
        for i in range(len(numbers)):
            if numbers[i] in map_num:
                return [numbers.index(target-numbers[i]) + 1, i+1]
            else:
                map_num[target - numbers[i]]  = numbers[i]

## 2 Pointer Approach only works in sorted array
def twoSum(self, numbers, target):
    n = len(numbers)-1
    l, r = 0, n
    while l <= r:
        if numbers[l] + numbers[r] == target:
            return [l+1,r+1]
        elif numbers[r]+numbers [l]> target:
            r = r - 1
        else:
            l = l + 1

'''