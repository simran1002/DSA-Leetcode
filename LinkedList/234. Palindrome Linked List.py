'''
Given the head of a singly linked list, return true if it is a 
palindrome
or false otherwise.
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        
        left, right = 0, len(list_vals) - 1
        while left < right and list_vals[left] == list_vals[right]:
            left += 1
            right -= 1
        return left >= right
    

Time Complexity: O(n)
Space Complexity: O(n)

