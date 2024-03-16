'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        d = {0: -1} 
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in d:
                max_length = max(max_length, i - d[count])
            else:
                d[count] = i
        
        return max_length


# Time Complexity: O(n)
# Space Complexity: O(n)