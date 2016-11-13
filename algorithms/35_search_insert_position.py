class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
        else:
            return left
    
print Solution().searchInsert([1,3,5,6], 5)
print Solution().searchInsert([1,3,5,6], 2)
print Solution().searchInsert([1,3,5,6], 7)
print Solution().searchInsert([1,3,5,6], 0)