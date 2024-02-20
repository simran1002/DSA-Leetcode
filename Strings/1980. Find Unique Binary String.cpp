'''Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n 
that does not appear in nums. If there are multiple answers, you may return any of them.
'''

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<int> st;

        for(string &num : nums) {
            st.insert(stoi(num, 0, 2));
        }

        int n = nums.size();

        string result ="";

        for(int number = 0; number<=n; number++) {

            if(st.find(number) == st.end()) {
                result = bitset<16>(number).to_string();

                return result.substr(16-n, n);
            }
        }

        return "";
    }
};

// Time Complexity: O(n * m)
// Space Complexity: O(n * m)


class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();

        string result;

        for(int i = 0; i<n; i++) {

            char ch = nums[i][i];

            result += (ch == '0') ? "1" : "0";

        }

        return result;
    }; 
};

// Time Complexity: O(n)
// Space Complexity: O(n)