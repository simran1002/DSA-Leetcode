/*
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
*/

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();

        unordered_map<int, int> mp;

        int i = 0;
        int j = 0;
        int result = 0;

        while(j < n) {

            mp[nums[j]]++;

            while(i < j && mp[nums[j]] > k) {
                mp[nums[i]]--;
                i++;
            }

            result = max(result, j - i + 1);
            j++;
        }

        return result;
    }
};


// Time Complexity: O(n)
// Space Complexity: O(n)