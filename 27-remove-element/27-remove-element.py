class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k =  0
        for i in range(0,len(nums)):
            if (nums[i]==val):
                nums[i] = 100
                k+=1
        nums.sort()
        return len(nums)-k