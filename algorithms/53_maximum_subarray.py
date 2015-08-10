class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        # discussion
        # adding the values until sum drops below 0, 
        # reset sequence if sum is negative.  
        sum_, max_ = 0, nums[0]
        for i in nums:
            sum_ += i
            max_ = max(max_, sum_)
            sum_ = max(sum_, 0)
        return max_
            
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])