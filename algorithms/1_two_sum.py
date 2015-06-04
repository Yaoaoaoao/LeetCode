class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        pool = {}
        for i, ni in enumerate(nums):
            nj = target - ni
            if nj in pool:
                return sorted([i+1, pool[nj]])
            else:
                pool[ni] = i+1
            
    
print Solution().twoSum([2, 7, 11, 15], 9) #  [1,2]
print Solution().twoSum([0,4,3,0], 0) # [1,4]