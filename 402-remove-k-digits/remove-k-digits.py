class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k>0:
                k-=1
                stack.pop()
            stack.append(i)

        stack=stack[:len(stack)-k]
        stack=''.join(stack)
        stack = stack.lstrip('0')

        return stack if stack else "0"