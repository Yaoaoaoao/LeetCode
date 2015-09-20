# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        
        # find midpoint
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        # divide
        left = self.sortList(head)
        right =self.sortList(slow)
        
        # merge
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        root = ListNode(0)
        node = root
        while left and right:
            if left.val <= right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            node.next = left
        if right:
            node.next = right
        return root.next
        

a = ListNode(1)
b = a.next = ListNode(3)
c = b.next = ListNode(2)
    
s = Solution().sortList(a)
while s:
    print s.val
    s = s.next
            