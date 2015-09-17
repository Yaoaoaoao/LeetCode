class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        l = len(nums)//2
        for n in nums:
            if not n in count:
                count[n] = 0
            count[n] += 1
            if count[n] > l:
                return n
        
        
        # or
        return sorted(nums)[len(nums)//2]  
        
print Solution().majorityElement([1, 5, 3, 4, 6, 6, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2])