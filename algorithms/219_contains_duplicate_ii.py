class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, e in enumerate(nums):
            if e in d and i-d[e] <= k:
                return True
            d[e] = i
        return False            
        
print Solution().containsNearbyDuplicate([1,2,1], 0)