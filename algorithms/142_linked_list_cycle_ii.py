# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # copy from 141
        # two pointer: slow and fast
        # fast = slow*2
        # if there is a cycle, then fast will catch up with slow (equal)
        ''' 
        142
        when slow reaches the start point of the cycle, 
        fast is already in the cycle. 
        fast will catch up with slow within one cycle.
        fast-slow <= cycle
        head --H--> Begin --E--> Meet ---> (Begin)
        slow = H+E
        fast = H+E+nC
        2slow = 2H + 2E = H+E+nC
        H = nC-E = (n-1)C + (C-E)
        Set two pointer, one start at head (a), the other start at meet point (b). when a and b meet, it's the loop start point. 
        '''
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                return None # no cycle
            if fast == slow:
                meet = fast
                break
        else:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        return slow