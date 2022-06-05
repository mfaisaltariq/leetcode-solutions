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