class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the nums first.
        nums = sorted(nums)
        return self.subset([], nums, [])
    
    def subset(self, soFar, rest, result):
        if len(rest) == 0:
            if soFar not in result:
                result.append(soFar)
        else:
            self.subset(soFar + [rest[0]], rest[1:], result)
            self.subset(soFar, rest[1:], result)
        return result
            
print Solution().subsetsWithDup([1,2,2])
print Solution().subsetsWithDup([4,4,4,1,4])