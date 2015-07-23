# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return None
        
        root = a = ListNode(0)
        root.next = head
        
        while a.next and a.next.next:
            b, c = a.next, a.next.next
            a.next, b.next, c.next = c, c.next, b
            a = a.next.next
        
        return root.next