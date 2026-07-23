class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMax = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMax:
                return [prevMax[diff],i]
            prevMax[n]=i