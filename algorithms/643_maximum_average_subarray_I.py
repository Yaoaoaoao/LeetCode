class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_ = sum(nums[:k]) * 1.0
        max_ = sum_
        for i in range(k, len(nums)):
            sum_ = sum_ - nums[i - k] + nums[i]
            max_ = max(max_, sum_)
        return max_ / k * 1.0


print Solution().findMaxAverage([4,2,1,3,3], 2) 
print Solution().findMaxAverage([0, 1, 1, 3, 3], 4)
print Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print Solution().findMaxAverage([3,3,4,3,0], 3)