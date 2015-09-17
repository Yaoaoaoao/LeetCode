class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        while v1 or v2:
            p1 = v1.pop(0) if v1 else 0
            p2 = v2.pop(0) if v2 else 0
            if p1 > p2:
                return 1
            elif p1 < p2:
                return -1
        return 0
        
print Solution().compareVersion("1.0.0", "1") #0
print Solution().compareVersion("01", "1") #0
print Solution().compareVersion("1.2", "1.10") # -1
print Solution().compareVersion('0.0.1', '0.0.0.1') # 1