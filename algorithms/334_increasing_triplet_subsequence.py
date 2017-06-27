class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # O(n) https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution
        first = second = float('inf')
        for n in nums:
            if n <= first: 
                first = n
            elif n <= second: 
                second = n
            else:
                return True
        return False
        
        # O(n^2)
        l = len(nums)
        if l <= 2:
            return False
        dp = [1] * l
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] >= 3:
                        return True
        return False


# print Solution().increasingTriplet([1, 2, 3, 4, 5])
# print Solution().increasingTriplet([5, 4, 3, 2, 1])
# print Solution().increasingTriplet([0, 4, 2, 1, 0, -1, -3])
print Solution().increasingTriplet([2, 1, 5, 0, 4, 6])
