# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 234_palindrome_linked_list.py
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        last = None
        while slow:
            tmp = slow.next
            slow.next = last
            last = slow
            slow = tmp
        # check palindrome
        left, right = head, last
        while left and right:
            # l0->ln -> l1->ln-1 -> l2...
            l1, ln1 = left.next, right.next
            if right == l1:
                break
            left.next, right.next = right, l1
            left, right = l1, ln1
          