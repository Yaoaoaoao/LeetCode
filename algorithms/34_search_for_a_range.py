class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left = self.binarySearch(nums, target-0.5)
        if nums[left] != target:
            return [-1, -1]
        nums.append(-1) 
        right = self.binarySearch(nums, target+0.5) -1
        return [left, right]
        
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
                
            
print Solution().searchRange([1], 1) # [0,0]
print Solution().searchRange([5,7,7,8,8,10], 8) # [3,4]