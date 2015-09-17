# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # two pointer: slow and fast
        # fast = slow*2
        # if there is a cycle, then fast will catch up with slow (equal)
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return False # no cycle
            if fast == slow:
                return True
        else:
            return False
        