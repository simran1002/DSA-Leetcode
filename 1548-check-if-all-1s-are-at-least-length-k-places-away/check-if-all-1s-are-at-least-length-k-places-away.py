class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # ones = []  

        # for i in range(len(nums)):
        #     if nums[i] == 1:  
        #         ones.append(i)

        # for j in range(len(ones) - 1): 
        #     if ones[j+1] - ones[j] - 1 < k:
        #         return False

        # return True

        prev = -1

        for i, val in enumerate(nums):
            if val == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        
        return True

