from typing import List
def searchInsert(nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = (start + end) // 2
            print(start, end, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid +1
            else:
                end = mid-1
                
        return end + 1

print(searchInsert([1,3,4,5,6,7],5))
print(searchInsert([1,3,5,6],2))