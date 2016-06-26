class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # NAIVE: O(nlogn)
        frequecy = {}
        for num in nums:
            if num not in frequecy:
                frequecy[num] = 0
            frequecy[num] += 1
        pairs = sorted(frequecy.items(), key=lambda x: x[1], reverse=True)[:k]
        return [p[0] for p in pairs]
    
print Solution().topKFrequent([-1,-1], 1)
print Solution().topKFrequent([1,1,1,2,2,3], 2) #[1,2]