def twoSum(nums: list[int], target: int) -> list[int]:
    seen ={}
    for i, value in enumerate(nums):
        remain = target-nums[i]
            
        if remain in seen:
            return [i,seen[remain]]
        seen[value] = i

print(twoSum([2,7,11,15], 9))
