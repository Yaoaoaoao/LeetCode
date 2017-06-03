class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num: parent_index
        union = {i: None for i in range(len(nums))}
        for i, n in enumerate(nums):
            if union[n] is None:
                parent, child = i, i
                while union[child] is None:
                    union[child] = parent
                    child = nums[child]
        from collections import Counter
        c = Counter(union.values()).values()
        return max(c)
                

print Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2])
