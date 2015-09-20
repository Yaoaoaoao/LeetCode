# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev = root = ListNode(0)
        root.next = head
        node = head
        repeatVal = None
        
        while node:
            if  node.val == repeatVal or (node.next and node.val == node.next.val):
                repeatVal = node.val
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
                
        return root.next
                
                
        