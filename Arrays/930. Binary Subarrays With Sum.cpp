/*
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
*/


class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int n = nums.size();
        unordered_map<int, int> mp;

        int result = 0;

        int currSum = 0;

        mp[0] = 1;

        for(int &num : nums) {
            currSum += num;

            int remaining_sum = currSum - goal;
            if(mp.find(remaining_sum) != mp.end()) {
                result +=mp[remaining_sum];
            }

            mp[currSum]++;
        }

        return result;
    }
};


// Time Complexity: O(n)
// Space Complexity: O(n)