class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i], nums[tmp-1] = nums[tmp-1], tmp
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        else:
            return n+1
    
print Solution().firstMissingPositive([1,2,0])
print Solution().firstMissingPositive([3,4,-1,1])