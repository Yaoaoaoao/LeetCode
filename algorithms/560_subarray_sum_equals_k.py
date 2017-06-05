class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum, count = 0, 0
        sum_ = {0: 1}
        for n in nums:
            current_sum += n
            if current_sum == k or current_sum - k in sum_:
                count += sum_[current_sum - k]
            sum_[current_sum] = sum_.get(current_sum, 0) + 1
        return count
        
        # O(n) + O(n**2)
        l = len(nums)
        sum_ = [0]
        for i in range(l):
            sum_.append(nums[i] + sum_[i])
        
        count = 0
        for i in range(l):
            for j in range(i+1, l+1):
                if sum_[j] - sum_[i] == k:
                    count += 1
        return count

print Solution().subarraySum([1, 1, 1], 2) # 2
print Solution().subarraySum([1,2,3], 3) # 2
print Solution().subarraySum([1], 0) # 0
print Solution().subarraySum([-1,-1,1], 0) # 1
print Solution().subarraySum([1], 1) # 1
print Solution().subarraySum([0,0,0,0,0,0,0,0,0,0], 0) # 55