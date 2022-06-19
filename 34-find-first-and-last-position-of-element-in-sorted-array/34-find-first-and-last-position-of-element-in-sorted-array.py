class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target in nums:
            res.append(nums.index(target))
            nums = nums[::-1]
            if target in nums:
                res.append(len(nums)-1-nums.index(target))
                return res
            else:
                res.append(-1)
                return res
        else:
            return [-1,-1]