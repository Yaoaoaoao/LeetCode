class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Solution
        end = k
        for i in xrange(k, len(arr)):
            delta = abs(arr[i] - x) - abs(arr[i - k] - x)
            if delta > 0:
                return arr[end - k:end]
            if delta < 0:
                end = i + 1
        return arr[end - k:end]


print Solution().findClosestElements([1], 1, 1) == [1]
print Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
print Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
print Solution().findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4) == [0, 1, 1, 1, 2, 3, 6, 7, 8]
print Solution().findClosestElements([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2) == [1, 3]
print Solution().findClosestElements([1, 2, 5, 5, 6, 6, 7, 7, 8, 9], 7, 7) == [5, 5, 6, 6, 7, 7, 8]
