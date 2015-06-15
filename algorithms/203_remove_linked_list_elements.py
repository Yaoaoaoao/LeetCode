# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        root = ListNode(0)
        root.next = head
        current, prev = head, root
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return root.next
    
        # JAVA recursive solution
        # RuntimeError: maximum recursion depth exceeded in cmp
        if head==None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head