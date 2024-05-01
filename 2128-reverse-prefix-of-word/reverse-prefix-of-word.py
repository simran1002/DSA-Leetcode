class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                reversed_part = word[:i+1][::-1]
                return reversed_part + word[i+1:]
        return word
