# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        x = self.get_num(l1)
        y = self.get_num(l2)
        return self.get_link_list(x+y)
    
    def get_num(self, l):
        n, next = [], l
        while next:
            n.append(next.val)
            next = next.next
        return int(''.join(map(str, n[::-1])))
    
    def get_link_list(self, z):
        next = None
        for i in list(str(z)):
            a = ListNode(i)
            a.next = next
            next = a
        return next