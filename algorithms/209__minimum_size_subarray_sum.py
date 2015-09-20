class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = total = 0
        count = len(nums) + 1 # if can't find a bigger sum, this count will return False
        for right, num in enumerate(nums):
            total += num
            while total >= s:
                count = min(count, right-left+1)
                total -= nums[left]
                left += 1
        return count if count <= len(nums) else 0
        
        # # dp O(nn) correct but TLE
        # if not nums:
        #     return 0
        # dp = []
        # for num in nums:
        #     if num >= s:
        #         return 1
        #     else:
        #         dp.append(num)
        # for length in range(2, len(nums)):
        #     for i in range(length-1, len(nums)):
        #         dp[i] += nums[i-length+1]
        #         if dp[i] >= s:
        #             return length
        # return 0
    