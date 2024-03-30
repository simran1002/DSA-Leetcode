'''
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.
'''

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_length = float('inf')
        for i in range(n):
            bitwise_or = 0
            for j in range(i, n):
                bitwise_or |= nums[j]
                if bitwise_or >= k:
                    min_length = min(min_length, j-i+1)
                    break
        return min_length if min_length != float('inf') else -1


# Time Complexity: O(n)
# Space Complexity: O(1)