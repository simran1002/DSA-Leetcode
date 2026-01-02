class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        # repetition = len(nums)//2
        # for i in nums:
        #     if nums.count(i)==repetition:
        #         return i