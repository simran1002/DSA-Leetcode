'''
You are given two strings order and s. All the characters of order are unique and were sorted
 in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically,
 if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.
'''

class Solution {
public:
    string customSortString(string order, string s) {
        int count[26] = {0};

        for(char&ch: s) {
            count[ch-'a']++;
        }

        string result ="";
        for(char &ch : order) {
            while(count[ch-'a'] > 0) {
                result.push_back(ch);
                count[ch-'a']--;
            }
        }

        for(char &ch: s) {
            if(count[ch-'a']>0) {
                result.push_back(ch);
            }
        }

        return result;
    }
};


// Time Complexity: O(n)
// Space Complexity: O(1)