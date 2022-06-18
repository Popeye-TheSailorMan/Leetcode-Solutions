import numpy as np
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        nums2 = list(set(nums))
        nums = sorted(nums)
        if (nums==sorted(nums2)):
            return False
        else:
            return True