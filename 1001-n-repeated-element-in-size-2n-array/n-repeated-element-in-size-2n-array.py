class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        repetition = len(nums)//2
        for i in nums:
            if nums.count(i)==repetition:
                return i