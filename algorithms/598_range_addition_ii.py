class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_m, min_n = m, n
        for op_m, op_n in ops:
            min_m = min(op_m, min_m)
            min_n = min(op_n, min_n)
        return min_m * min_n 
                