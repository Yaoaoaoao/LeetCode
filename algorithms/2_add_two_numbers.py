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
        
# Aug13
root = ListNode(0)
        node = root
        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit > 9:
                digit = digit % 10
                carry = 1
            else:
                carry = 0
            node.next = ListNode(digit)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            if carry > 0:
                digit = l1.val + carry
                if digit > 9:
                    digit = digit % 10
                    carry = 1
                else:
                    carry = 0
                node.next = ListNode(digit)
                node = node.next
                l1 = l1.next
            else:
                node.next = l1
                break
        while l2:
            if carry > 0:
                digit = l2.val + carry
                if digit > 9:
                    digit = digit % 10
                    carry = 1
                else:
                    carry = 0
                node.next = ListNode(digit)
                node = node.next
                l2 = l2.next
            else:
                node.next = l2
                break
        if carry > 0:
            node.next = ListNode(carry)
        return root.next
