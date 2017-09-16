class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums = sorted(nums)
        count = 0
        for i in range(l - 2):
            k = i + 2
            for j in range(i + 1, l - 1):
                while k < l and nums[i] + nums[j] > nums[k]:
                    k += 1
                if k > j:
                    count += k - j - 1
        return count


print Solution().triangleNumber([2, 2, 3, 4])
print Solution().triangleNumber([0, 1, 1, 1])
print Solution().triangleNumber([82,15,23,82,67,0,3,92,11]) # 17
