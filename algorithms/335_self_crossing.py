class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: list[int]
        :rtype: bool
        Case 1:
        ---1---
        |     |
        2     |
        |     |
        ---3--|--
              0
        Case 2:
        ---1---
        |     | 
        2     |
        |     |
        -3----0--
        Case 3:
        ---1---
        |     | 
        2   -----5-
        |     |   |
        |     0   |
        |         4
        ---3-------
        """
        for i in range(3, len(x)):
            # Case 1: x1<=x3 and x2<=x0
            if x[i-2] <= x[i] and x[i-1] <= x[i-3]:
                return True
            # Case 2: x1==x3 and x4 >= x2-x0
            if i > 3 and x[i-1] == x[i-3] and x[i] >= x[i-2] - x[i-4]:
                return True
            # Case 3: x3>=x1 and x4<=x2 and x5 >= x3-x1 and x4 >= x2-x0
            if i > 4 and x[i-2] >= x[i-4] and x[i-1] <= x[i-3] \
                     and x[i] >= x[i-2]-x[i-4] and x[i-1] >= x[i-3]-x[i-5] :
                return True
        else:
            return False
            


print Solution().isSelfCrossing([2, 1, 1, 2]) # t
print Solution().isSelfCrossing([1, 2, 3, 4]) # f
print Solution().isSelfCrossing([1, 1, 1, 1]) # t
print Solution().isSelfCrossing([3, 3, 4, 2, 2]) # f
