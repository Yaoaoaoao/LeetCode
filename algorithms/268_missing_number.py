class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # swap number to correct index
        nums.append(-1)
        for n in range(len(nums)):
            while nums[n] >= 0 and nums[n] != n:
                tmp = nums[n]
                nums[n], nums[tmp] = nums[tmp], nums[n]
        return nums.index(-1)
            
            
    
print Solution().missingNumber([0,1,3])
print Solution().missingNumber([2,0])
print Solution().missingNumber([4,3,5,2,1])