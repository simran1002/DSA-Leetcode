'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        i1=i2=0
        while i1<n1 and i2<n2:
            if nums1[i1]==nums2[i2]:
                return nums1[i1]
            elif nums1[i1]<nums2[i2]:
                i1=i1+1
            else:
                i2=i2+1
        return -1
    
# Time Complexity: O(n1+n2)
# Space Complexity: O(1)