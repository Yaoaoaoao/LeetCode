### Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k<2:
            return head
        
        root = head
        # check k nodes
        for i in range(k-1):
            root = root.next
            if not root:
                return head
         
        prev, cur = None, head 
        for i in range(k):
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        
        head.next = self.reverseKGroup(cur, k)
            
        return root
