import numpy as np
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.remove(nums[i])
        #         print(nums)
        #     else:
        #         i+=1
        # return len(nums)
        seen = []
        for i in range(0,len(nums)):
            if nums[i] in seen:
                nums[i] = 200
            else:
                seen.append(nums[i])
        nums.sort()
        return len(seen)
        
        
        