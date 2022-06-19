class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            i = 0
            while i<len(nums):
                if(nums[i]>target):
                    return nums.index(nums[i])
                i = i+1
            return len(nums)