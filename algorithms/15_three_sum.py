class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        n = sorted(nums)
        rtn = []
        
        for i in range(len(n)-2):
            j = i+1
            k = len(n)-1
            
            while j < k:
                sum_ = n[i]+n[j]+n[k]
                if sum_ == 0:
                    rtn.append((n[i], n[j], n[k]))
                if sum_ > 0: # means k is too large
                    k -= 1
                else: # means j is too small
                    j += 1
        
        return list(set(rtn))
                    
    
print Solution().threeSum([0,0])
print Solution().threeSum([-1, 0, 1, 2, -1, -4])