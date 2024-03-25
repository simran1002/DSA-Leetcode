'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        duplicates = []
        for i in range(n):
            if nums[i] in s:
                duplicates.append(nums[i])
            else:
                s.add(nums[i])
        
        return duplicates
            

# Time Complexity: O(n)
# Space Complexity: O(1)