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
