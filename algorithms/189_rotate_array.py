class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if k > 0 and len(nums)>1:
            k %= len(nums)
            
        # solution 1
            nums = nums[k:]+nums[:k]
        
        return nums

print Solution().rotate([1,2], 1)