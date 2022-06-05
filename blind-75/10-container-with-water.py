from typing import List
def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    area = 0

    while l < r:
        new_area = (r - l ) * min(height[l], height[r])
        area = max(area, new_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return area

print(maxArea([1,8,6,2,5,4,8,3,7]))
