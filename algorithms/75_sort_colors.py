class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, second, i = 0, len(nums)-1, 0
        while i <= second and zero <= second:
            if nums[i] == 0 and i >= zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            elif nums[i] == 2 and i <= second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            else:
                i += 1
        # return nums

print Solution().sortColors([0])
print Solution().sortColors([0,1,2])
print Solution().sortColors([1,2,1,2,1,2,1,2,0,0,0,0])