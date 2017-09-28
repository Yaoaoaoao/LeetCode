class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = len(nums)
        result = [''] * l
        sort = sorted(enumerate(nums), key=lambda x:x[1], reverse=True)
        for rank, (idx, score) in enumerate(sort):
            if rank == 0:
                val = 'Gold Medal'
            elif rank == 1:
                val = 'Silver Medal'
            elif rank == 2:
                val = 'Bronze Medal'
            else: 
                val = str(rank+1)
            result[idx] = val
        return result


print Solution().findRelativeRanks([5, 4, 3, 2, 1])
