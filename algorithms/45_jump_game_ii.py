class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy
        if len(nums)<=1:
            return 0
        step, maxReach, nextReach = 1, nums[0], nums[0]
        for i in range(1,len(nums)):
            # reach the end
            if maxReach >= len(nums)-1:
                return step
            # update to nextReach
            if i > maxReach: 
                maxReach = nextReach
                step += 1
            
            nextReach = max(nextReach, i+nums[i])
        return step
                
            
print Solution().jump([2,3,1,1,4]) #2
print Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]) #2
            
        