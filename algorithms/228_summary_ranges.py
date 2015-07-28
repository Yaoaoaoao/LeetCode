class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) <= 1:
            return ["%d" % d for d in nums]
        
        ranges = []
        left = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                ranges.append((left, nums[i-1]))
                left = nums[i]
        ranges.append((left, nums[i]))
        
        rtn = []
        for (a,b) in ranges:
            if a != b:
                rtn.append("%d->%d" % (a,b))
            else:
                rtn.append("%d" % (a))
        return rtn     
    
print Solution().summaryRanges([])
print Solution().summaryRanges([-1])
print Solution().summaryRanges([0,1,2,4,5,7])
print Solution().summaryRanges([0,1,2,4,6,7])