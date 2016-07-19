# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def startBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        head = root
        for i in range(m-1):
            head = head.next
        # root - 1(head) - 2 - 3 - 4 - 5
        start = head.next # 2
        if not start or not start.next:
            return root.next
        remain = start.next # 3
        # 1head - 2start - 3remain -  
        for i in range(n-m):
            if not start.next:
                break
            start.next = remain.next    # 1head - 2start - 
            remain.next = head.next     # - 3remain - 2start -
            head.next = remain          # 1head - 3remain - 2start -
            remain = start.next
        return root.next
