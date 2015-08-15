class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums)==0:
            return 0
        dp = {}
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[len(nums)-1]
    
print Solution().rob([])
print Solution().rob([1,2,3,4,5,6,7])