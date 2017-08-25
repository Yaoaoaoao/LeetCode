class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Brute force: time O(n), space O(n)
        s = {}
        dup, missing = 0, 0
        for n in nums:
            if n in s:
                dup = n
            else:
                s[n] = True
        for i in range(1, len(nums) + 1):
            if i not in s:
                missing = i
        return [dup, missing]


print Solution().findErrorNums([1, 2, 2, 4])
