class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start, end = -1, -1
        max_, min_ = nums[0], nums[n - 1]
        for i in range(1, n):
            max_ = max(max_, nums[i])
            if nums[i] < max_:
                end = i
            min_ = min(min_, nums[n - i - 1])
            if nums[n - i - 1] > min_:
                start = n - i - 1

        if start == -1:
            return 0

        return end - start + 1


print Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
print Solution().findUnsortedSubarray([1, 3, 2, 2, 2])
print Solution().findUnsortedSubarray([1, 2, 3, 4])
print Solution().findUnsortedSubarray([1])
