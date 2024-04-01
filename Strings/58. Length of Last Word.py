'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring
 consisting of non-space characters only.
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.split()
        n=len(d[-1])
        return n
        

# Time Complexity: O(1)
# Space Complexity: O(n)