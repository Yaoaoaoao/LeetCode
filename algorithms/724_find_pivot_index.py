class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # slow
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i + 1:]):
        #         return i
        # return -1

        # faster
        if len(nums) < 1:
            return -1
        left, right = 0, sum(nums) - nums[0]
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1


print Solution().pivotIndex([1, 7, 3, 6, 5, 6])
print Solution().pivotIndex([1, 2, 3])
print Solution().pivotIndex([-1, -1, -1, 0, 1, 1])
