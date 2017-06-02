class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        x, y = len(nums), len(nums[0])
        if x * y != r * c:
            return nums
        flat = []
        for i in nums:
            flat.extend(i)
        reshape = []
        for i in range(r):
            reshape.append(flat[i * c:i * c + c])
        return reshape


print Solution().matrixReshape([[1, 2], [3, 4]], 4, 1)
