class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if len(nums) == 1:
            return True
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            count += 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if count >= 1:
                    return False
                if nums[i + 1] > nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                count += 1
        if count <= 1:
            return True


print Solution().checkPossibility([1])
print Solution().checkPossibility([1, 2])
print Solution().checkPossibility([2, 1])
print Solution().checkPossibility([4, 2, 3])
print Solution().checkPossibility([4, 2, 1])
print Solution().checkPossibility([3, 4, 2, 3])
print Solution().checkPossibility([3, 4, 2, 5])
print Solution().checkPossibility([1, 4, 2, 5])
