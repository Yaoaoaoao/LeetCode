# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        # ROOT->1->2->3->4->5->NULL
        # ROOT  1->2->3  4->5  NULL
        #          SLOW  FAST
        # total fast go: n
        # total slow go: n-k
        
        if not head or k==0:
            return head

        slow = fast = head
        n = 1
        while fast and fast.next:
            n += 1
            fast = fast.next
        
        k %= n
        if k == 0:
            return head
        
        k = n-k
        while k:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        fast.next = root.next
        root.next = slow.next
        slow.next = None
        
        return root.next
        
        