# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # discussion clever solution # 356ms
    def getIntersectionNode(self, headA, headB):
        # L1 and L2 have the same tail after the intersection point
        # L1+L2 and L2+L1 will be same after the intersection point
        # L1+L2: pta pointer
        # L2+L1: ptb pointer
        pta, ptb = headA, headB
        flag = True # a flag for L1+L2. ensure only loop L2 once
        while pta and ptb:
            if pta == ptb:
                return pta
            
            pta = pta.next
            if not pta: # L1 finish, start L2
                if flag:
                    pta = headB
                    flag = False
                else:
                    return None
                
            ptb = ptb.next
            if not ptb: # L2 finish, start L2
                ptb = headA
        return None
        
    
    
    # # discussion 360ms solution
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     curA, curB = headA, headB
    #     lenA, lenB = 0, 0
    #     while curA:
    #         curA = curA.next
    #         lenA += 1
    #     while curB:
    #         curB = curB.next
    #         lenB += 1
    #     curA, curB = headA, headB
    #     if lenA > lenB: # B in A
    #         for i in range(lenA-lenB):
    #             curA = curA.next
    #     elif lenA < lenB:
    #         for i in range(lenB-lenA):
    #             curB = curB.next
    #     while curA != curB:
    #         curA = curA.next
    #         curB = curB.next
    #     return curA
            