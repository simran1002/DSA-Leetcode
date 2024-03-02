'''
Given an integer array nums sorted in non-decreasing order,
 return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums[x]=nums[x]*nums[x]
        nums.sort()
        return nums
        

# Time Complexity : O(nlogn)
# Space Complexity : O(1)