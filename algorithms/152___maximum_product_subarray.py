class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        big = small = 0
        max_ = 0
        for i in range(length):
            if nums[i] < 0:
                big, small = small, big
            big = max(big*nums[i], nums[i])
            small = min(small*nums[i], nums[i])
            max_ = max(max_, big)
        return max_
        
        
        # dp O(n) space O(nn) time -> TLE
        # if not nums:
        #     return 0
        # length = len(nums)
        # if length == 1:
        #     return nums[0]
        # dp = [i for i in nums]
        # for i in range(1, length):
        #     for j in range(i, length):
        #         dp[j] = max(dp[j], dp[j-1]*nums[j])
        # return max(dp)

# print Solution().maxProduct([2,0])
print Solution().maxProduct([2,3,-2,4])