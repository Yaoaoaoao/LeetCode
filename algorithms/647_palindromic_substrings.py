class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        # Brute force: O(n**2)
        count = 0
        L = len(s)
        for l in range(1, L + 1):
            for i in range(l, L + 1):
                subs = s[i - l: i]
                if subs == subs[::-1]:
                    count += 1
        return count


print Solution().countSubstrings('abc')
print Solution().countSubstrings('aba')
print Solution().countSubstrings('aaa')
