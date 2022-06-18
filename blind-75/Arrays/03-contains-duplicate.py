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