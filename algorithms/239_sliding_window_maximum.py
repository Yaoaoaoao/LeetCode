class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        # linear
        # use deque/list to store the max/candidates indexes
        if len(nums) == 0:
            return []
        
        from collections import deque
        dq = deque()
        for i in range(k):
            # remove previous elements if the new element is bigger than them
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        # max value will be at the beginning
        result = [nums[dq[0]]]
        
        # slide the window
        for i in range(k, len(nums)):
            # remove element not in current window
            while dq and dq[0] < i-k+1 :
                dq.popleft()
            # maintain the deque 
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            result.append(nums[dq[0]])
        return result
            
        # # naive O(k*n)
        # return [max(nums[i:i+k]) for i in range(0, len(nums)-k+1)] if len(nums)>0 else []
     
print Solution().maxSlidingWindow([], 0) # []
print Solution().maxSlidingWindow([1,-1], 1)  # [1,1]
print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]