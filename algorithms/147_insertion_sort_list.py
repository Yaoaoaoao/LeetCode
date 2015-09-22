# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def print_list(s):
    while s:
        print s.val,
        s = s.next
    print 

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        root = ListNode(0)
        root.next = head
        
        sortedEnd = head
        unsortedHead = head.next
        
        while unsortedHead:
            if unsortedHead.val < sortedEnd.val:
                sortedEnd.next = unsortedHead.next
                curr = root
                while curr.next and curr.next.val < unsortedHead.val:
                    curr = curr.next
                currNext = curr.next
                curr.next = unsortedHead
                unsortedHead.next = currNext
                unsortedHead = sortedEnd.next
            else:
                sortedEnd = unsortedHead
                unsortedHead = unsortedHead.next
            
        return root.next
    
    
a = ListNode(3)
b = a.next = ListNode(2)
c = b.next = ListNode(5)
d = c.next = ListNode(7)
e = d.next = ListNode(9)
f = e.next = ListNode(1)
g = f.next = ListNode(4)
h = g.next = ListNode(6)
i = h.next = ListNode(8)

s = Solution().insertionSortList(a)
print_list(s)