# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = h1 = ListNode(0)
        big = h2 = ListNode(0)
        node = head
        while node:
            if node.val < x:
                h1.next = node
                h1 = h1.next
            else:
                h2.next = node
                h2 = h2.next
            node = node.next
        h2.next = None
        h1.next = big.next
        return small.next