class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        ans = 0
        for i in count:
            if i + 1 in count:
                ans = max(ans, count[i] + count[i+1])
        return ans
        
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        ans = 0
        for i in count:
            if i + 1 in count:
                ans = max(ans, count[i] + count[i+1])
        return ans