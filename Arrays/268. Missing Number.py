'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for x in range(len(nums)+1):
            if x not in nums:
                return x
                
#Time Complexity: O(n^2)
#Space Complexity: O(1)
