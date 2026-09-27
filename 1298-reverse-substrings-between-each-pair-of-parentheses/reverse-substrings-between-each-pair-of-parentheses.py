class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until we find the opening bracket '('
                current_chars = []
                while stack and stack[-1] != '(':
                    current_chars.append(stack.pop())
                
                # Remove the '(' from the stack
                if stack and stack[-1] == '(':
                    stack.pop()
                
                # Push the reversed characters back onto the stack
                for c in current_chars:
                    stack.append(c)
            else:
                stack.append(char)
                
        return "".join(stack)