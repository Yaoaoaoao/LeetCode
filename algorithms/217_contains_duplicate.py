class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        A = {}
        for i in nums:
            if i in A:
                return True
            else:
                A[i] = None
        else:
            return False
        
        # simple one line solution
        return len(nums) != len(set(nums))
        
print Solution().containsDuplicate([]) #False
print Solution().containsDuplicate([0]) #False
print Solution().containsDuplicate([3,3]) #True
print Solution().containsDuplicate([1,2,3]) #False