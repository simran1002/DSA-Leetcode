'''
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
'''


class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        
        result = [s[0]]
        for x in range(1, len(s)):
            if result and abs(ord(result[-1]) - ord(s[x])) == 32:
                result.pop()
            else:
                result.append(s[x])
        return ''.join(result)


Time Complexity: O(n)
Space Complexity: O(n)