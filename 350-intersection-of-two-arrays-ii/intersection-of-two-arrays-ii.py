from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        for num in nums1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        
        return result
