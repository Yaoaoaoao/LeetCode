class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]:
                    # pivot on the right side
                    if nums[left] <= target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    # pivot in this side
                    if nums[mid] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        else:
            return -1
                        
                    
    
print Solution().search([4,5,6,7,0,1,2], 0)