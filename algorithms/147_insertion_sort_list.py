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
        beginOfUnsort = root = ListNode(0)
        root.next = head
        
        while beginOfUnsort and beginOfUnsort.next:
            
            # get the node out of the linked list
            enfOfSort = beginOfUnsort # end of sorted list
            current = beginOfUnsort.next 
            
            if current.val < enfOfSort.val:
                # insert the node to the correct position
                unsorted = beginOfUnsort.next.next # start of unsorted list
                beginOfUnsort = beginOfUnsort.next
                
                # connect the sorted and unsorted part
                enfOfSort.next = unsorted
                # put node into the correct position
                check = root
                # check the node from root
                while check.next and current.val >= check.next.val:
                    check = check.next
                # insert current between check and check.next
                nextNode = check.next
                check.next = current
                current.next = nextNode
            else:
                # already sorted, enter next
                beginOfUnsort = beginOfUnsort.next
            
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