class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Run two round: 1 to n-1, 2 to n
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def dp_rob(start):
            dp = []
            dp.append(nums[start])
            for i in range(start+1, start+len(nums)-1):
                if i == start+1:
                    dp.append(max(nums[start], nums[start+1]))
                else:
                    dp.append(max(nums[i]+dp[i-2-start], dp[i-1-start]))
            return dp[-1]
        
        # rob the first house
        dp_first = dp_rob(0)

        # rob the last house
        dp_last = dp_rob(1)
        
        return max(dp_first, dp_last)
    
print Solution().rob([1,1,1])
print Solution().rob([1,3,5,7,11])