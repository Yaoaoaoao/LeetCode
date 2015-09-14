class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # my 84ms solution
        if not nums:
            return 0
        i = j = 1
        dup = 0
        while i < len(nums):
            if nums[i] == nums[i-1]:
                dup += 1
            else:
                dup = 0
            if dup < 2:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
        
        
        # discussion 80ms
        # i = 0
        # for n in nums:
        #     if i < 2 or n > nums[i-2]:
        #         nums[i] = n
        #         i += 1
        # return i


print Solution().removeDuplicates([1,1,1,1])
print Solution().removeDuplicates([1,1,1,2,2,3])