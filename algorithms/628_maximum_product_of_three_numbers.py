class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if all positives: pick 3 largest
        # if has negative, pick 2 or 0 
        # -1 < x < 1
        # --+ , +++ 
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[-1] * nums[0] * nums[1])
        
        # brute force O(n^3)
        nums = sorted(nums, key=lambda x: abs(x), reverse=True)
        l = len(nums)
        maxp = float('-inf')
        for a in range(l-2):
            for b in range(a+1, l-1):
                for c in range(b+1, l):
                    maxp = max(nums[a]*nums[b]*nums[c], maxp)
        return maxp


print Solution().maximumProduct([-5, -4, 0, 1, 2, 3])