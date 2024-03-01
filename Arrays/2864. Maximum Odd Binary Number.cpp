'''
You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that
can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.
'''


class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.length();

        string result = string(n, '0');

        int i = 0;

        for(char &ch : s) {
            if(ch == '1') {
                if(result[n-1] == '1') { 
                    result[i] = '1';
                    i++;
                } else {
                    result[n-1] = '1';
                }
            }
        }

        return result;
    }
};


// Time Complexity: O(n)
// Space Complexity: O(n)


class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.length();
        
        string result = string(n, '0');
        
        int count_1 = count(s.begin(), s.end(), '1');
        
        int j = 0;
        
        while(count_1 > 1) {
            result[j] = '1';
            j++;
            
            count_1--;
        }
        
        result[n-1] = '1';
        return result;
    }
};



// Time Complexity: O(n)
// Space Complexity: O(n)