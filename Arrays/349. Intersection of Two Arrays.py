'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        l=[]
        if n1>=n2:
            for i in nums1:
                if i in nums2:
                    if i not in l:
                       l.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    if i not in l:
                       l.append(i)
        return l 

        
# Time Complexity: O(n*m)
# Space Complexity: O(min(n,m))