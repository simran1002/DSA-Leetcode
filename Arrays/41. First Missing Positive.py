'''
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
'''

class Solution:
    def firstMissingPositive(self, A: list[int]) -> int:
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
        
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)

        for i in range(1, len(A) + 1):
            if A[i - 1] >= 0:
                return i
        return len(A) + 1 

# Time Complexity: O(n)
# Space Complexity: O(1)