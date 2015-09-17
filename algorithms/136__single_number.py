class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # x1 = x0 XOR y
        # x2 = x1 XOR y
        # then x0 == x2
        result = 0
        for num in nums:
            result ^= num
        return result