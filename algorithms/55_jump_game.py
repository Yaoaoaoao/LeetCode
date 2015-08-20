class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        # greedy
        jump = 0
        for i in range(len(nums)):
            if jump < i:
                return False
            else:
                jump = max(jump, i+nums[i])
        return True
            

print Solution().canJump([0]) # true
print Solution().canJump([1]) # true
print Solution().canJump([2,0]) # true
print Solution().canJump([2,3,1,1,4]) # true
print Solution().canJump([3,2,1,0,4]) # false
print Solution().canJump([5,9,3,2,1,0,2,3,3,1,0,0]) # true
