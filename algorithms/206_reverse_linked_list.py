# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # iteratively
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        node, prev = head, None
        while node:
            node_next = node.next
            node.next = prev
            prev = node
            node = node_next
        return prev


    # recursively
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_list(head, None)
        
    def reverse_list(self, node, prev):
        if not node:
            return prev
        else:
            next_node = node.next
            node.next = prev
            return self.reverse_list(next_node, node)