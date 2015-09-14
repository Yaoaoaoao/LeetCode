def isBadVersion(version):
    return version == 1

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        left, right = 1, n
        while left < right:
            mid = (right+left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left
    
print Solution().firstBadVersion(2)