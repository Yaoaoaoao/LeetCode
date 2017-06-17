class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        n = sorted(nums)
        i, j, result = 0, 1, set()
        while i < l and j < l:
            if i == j:
                j += 1
                continue
            diff = abs(n[i]-n[j])
            if diff == k:
                result.add((n[i], n[j]))
                j += 1
            elif diff > k:
                i += 1
            else:
                j += 1
        return len(result)

print Solution().findPairs([3, 1, 4, 1, 5], 2)
print Solution().findPairs([1, 2, 3, 4, 5], 1)
print Solution().findPairs([1, 3, 1, 5, 4], 0)
