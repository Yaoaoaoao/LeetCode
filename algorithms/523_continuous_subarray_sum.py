class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod = {0: -1}
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if k != 0:
                sum_ %= k
            if sum_ in mod:
                if i - mod[sum_] > 1:
                    return True
            else:
                mod[sum_] = i
        return False


print Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
print Solution().checkSubarraySum([0, 0], 0)