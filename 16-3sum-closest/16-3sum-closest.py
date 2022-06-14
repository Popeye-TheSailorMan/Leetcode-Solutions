class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0]+nums[1]+nums[2]
        nums = sorted(nums)
        for i in range(len(nums)-2):
            a = i+1
            b = len(nums)-1
            
            while b>a:
                ans = nums[i]+nums[a]+nums[b]
                
                if ans>target:
                    b=b-1
                else:
                    a= a+1
                
                if (abs(res-target)>abs(ans-target)):
                    res = ans
        return res
            