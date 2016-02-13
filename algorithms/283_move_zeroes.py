class Solution(object):
    def moveZeroes(self, nums):
        # one line solution
        return nums.sort(cmp=lambda a, b: 0 if b else -1)
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # idea: find 0, del the zero and count how many zeroes are deleted. 
        # append 0 at the end of the list.  Use extra space??
        count_zero = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                count_zero += 1
                del nums[i]
            else:
                i += 1
        nums += [0] * count_zero
        return nums
    
print Solution().moveZeroes([0,1,0,3,12])
    