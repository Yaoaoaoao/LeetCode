class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, b = len(A), len(B)
        q = (b - 1) / a + 1
        if B in A * q:
            return q
        elif B in A * (q + 1):
            return q + 1
        else:
            return -1