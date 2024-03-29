/*
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.
*/


class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int maxE = *max_element(begin(nums), end(nums));

        int n = nums.size();
        int i = 0;
        int j = 0;

        long long result = 0;
        int countMax = 0;

        while(j < n) {
            if(nums[j] == maxE) {
                countMax++;
            }

            while(countMax >= k) {
                result += n-j;

                if(nums[i] == maxE) {
                    countMax--;
                }
                i++;
            }
            j++;
        }
        return result;
    }
};


Time Complexity: O(n)
Space Complexity: O(1)