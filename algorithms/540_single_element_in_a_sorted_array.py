class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) / 2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and \
                (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid
                else:
                    right = mid


print Solution().singleNonDuplicate([0, 1, 1])  # 0
print Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4])  # 2
print Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])  # 2
print Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])  # 10
