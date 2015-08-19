# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        # reverse the second half
        # a->b->c->b->a
        # a->b->c->b<-a
        # find mid point
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
        while last:
            if head.val != last.val:
                return False
            else:
                head = head.next
                last = last.next
        return True