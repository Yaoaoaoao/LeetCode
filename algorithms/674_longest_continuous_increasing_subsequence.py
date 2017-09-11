class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        longest, curr = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1
        return longest


print Solution().findLengthOfLCIS([1, 3, 5, 4, 7])
print Solution().findLengthOfLCIS([2, 2, 2, 2, 2])
