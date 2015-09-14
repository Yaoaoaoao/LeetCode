class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse=True)
        h = 0
        for c in range(len(citations)):
            if citations[c] >= c+1:
                h = c+1
            else:
                break
        return h
        
        
print Solution().hIndex([])
print Solution().hIndex([0])
print Solution().hIndex([100])
print Solution().hIndex([3, 0, 6, 1, 5])
print Solution().hIndex([300, 0, 600, 100, 500])