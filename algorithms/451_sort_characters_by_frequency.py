class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cnt = Counter(s).items()
        c = sorted(cnt, key=lambda x: x[1], reverse=True)
        rst = ''
        for i, j in c:
            rst += i * j
        return rst


print Solution().frequencySort('')
print Solution().frequencySort('tree')
