/*
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
*/


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_counter = Counter(nums)
        
        max_frequency = max(freq_counter.values())
        
        max_freq_elements = [num for num, freq in freq_counter.items() if freq == max_frequency]
        
        total_frequency = max_frequency * len(max_freq_elements)
        
        return total_frequency


// Time Compexity: O(n)
// Space Compexity: O(n+k)