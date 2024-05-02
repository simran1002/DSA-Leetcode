class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,0,-1):
            if nums[i]*-1 in nums:
                return nums[i]
        return -1