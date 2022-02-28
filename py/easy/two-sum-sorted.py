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