class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D=dict()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in D:
                return [D[diff],i]
            D[nums[i]]=i
        

        