class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        length = len(nums)
        if length <= 1:
            return 0
        if length == 2:
            return 0 if nums[0]>nums[1] else 1
        for i in range(length):
            left = i==0 or (i>0 and nums[i] > nums[i-1])
            right = i==length-1 or (i<length and nums[i] > nums[i+1])
            if left and right:
                return i
        return 0
    
print Solution().findPeakElement([1,2,3])