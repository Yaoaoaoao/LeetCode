class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        words = sorted(d, key=lambda x: (-len(x), x))
        ls = len(s)
        for word in words:
            lw = len(word)
            x, y = 0, 0
            while x < lw and y < ls:
                if word[x] == s[y]:
                    x += 1
                y += 1
            if x == lw:
                return word
        return ''


print Solution().findLongestWord('abpcplea', ["ale", "apple", "monkey", "plea"])
print Solution().findLongestWord('abpcplea', ["b", "c", "a"])