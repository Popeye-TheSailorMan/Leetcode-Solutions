import numpy as np
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        f_area = 0
        while i<j:
            curr_area = (j-i)*min(height[i],height[j])
            f_area = curr_area if f_area<curr_area else f_area
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return f_area