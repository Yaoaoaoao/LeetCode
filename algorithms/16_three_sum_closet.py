class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        n = sorted(nums)
        rtn = sum(nums[:3])
        for i in xrange(len(n)-2):
            j = i+1
            k = len(n)-1
            
            while j<k:
                sum_ = n[i]+n[j]+n[k]
                if abs(sum_-target) < abs(rtn-target):
                    rtn = sum_
                
                if sum_>target:
                    k -= 1
                else:
                    j += 1
        return rtn

print Solution().threeSumClosest([-1,2,1,-4], 1)