'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            else:
                num_set.add(num)
        

# Time Complexity: O(n)
# Space Complexity: O(n)
        