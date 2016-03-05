class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # DISCUSSION SOLUTION
        result = []
        # Left to me.
        product = 1
        for i in range(len(nums)):
            result.append(product)
            product *= nums[i]
        # Right to me. 
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result
        
        # NAIVE SOLUTION: calculate product of all elements and divide the num[i]
        # Got Time Limit Exceeded.
        return [reduce(lambda x, y: x*y, nums[:i]+nums[i+1:]) for i in range(len(nums))]
    
print Solution().productExceptSelf([1,2,3,4]) # [24,12,8,6]
print Solution().productExceptSelf([1,0]) # [0, 1]