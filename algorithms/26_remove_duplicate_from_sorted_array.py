class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # cheat and easy way..
        # nums[:] = sorted(set(nums))
        # return len(nums)
        
        if not nums:
            return 0
        i, j = 1, 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j