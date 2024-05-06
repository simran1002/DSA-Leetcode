class Solution:
    def removeNodes(self, head):
        if not head:
            return head
        head.next = self.removeNodes(head.next)
        if head.next and head.next.val > head.val:
            return head.next
        else:
            return head

