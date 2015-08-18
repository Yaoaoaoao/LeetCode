class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        result = {}
        for i in nums:
            if i in result:
                del result[i]
            else:
                result[i] = True
        return result.keys()
    
print Solution().singleNumber([1, 2, 1, 3, 2, 5])