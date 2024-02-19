#STATEMENT:-
'''
Given an array of integers called nums, you can perform the following operation while nums contains at least 2 elements:
#Choose the first two elements of nums and delete them.
The score of the operation is the sum of the deleted elements.
Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
Return the maximum number of operations possible that satisfy the condition mentioned above.
'''

class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        n=len(nums)
        count=1
        sum=nums[0]+nums[1]
        for x in range(2,n-1,2):
            a=nums[x]+nums[x+1]
            if a!=sum:
                break
            else:
                count=count+1
        return count
    
# Time Complexity: O(n)
# Space Complexity: O(1)
            
            
            