/*
Given an array of integers nums and an integer k, return the number of contiguous subarrays where 
the product of all the elements in the subarray is strictly less than k.
*/

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n = nums.size();
        if(k<=1) {
            return 0;
        }

        int i = 0;
        int j = 0;

        int count = 0;
        int prod = 1;

        while(j < n) {
            prod *= nums[j];

            while(prod >= k) {
                prod /= nums[i];
                i++;
            }

            count += (j-i+1);
            j++;
        }

        return count;
    }

};


// Time Complexity: O(n)
// Space Complexity: O(1)