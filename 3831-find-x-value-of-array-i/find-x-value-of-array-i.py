class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        # dp[r] stores the number of subarrays ending at the previous position 
        # whose product modulo k equals r
        dp = [0] * k
        
        for num in nums:
            val_mod = num % k
            next_dp = [0] * k
            
            # Start a new single-element subarray ending at the current index
            next_dp[val_mod] += 1
            
            # Extend all existing subarrays ending at the previous index
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val_mod) % k] += dp[r]
            
            dp = next_dp
            
            # Accumulate the counts for all remainders into the answer array
            for r in range(k):
                result[r] += dp[r]
                
        return result