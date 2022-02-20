from typing import List
def maxArea(height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        
        while left <= right:
            temp = min(height[left], height[right]) * (right - left)
            print(area, temp)
            if temp > area:
                area = temp
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return area

print(maxArea([1,8,6,2,5,4,8,3,7]))