class Solution(object):
    def combinationSum4(self, nums, target):
        """
        dp[i] = n means: there are n possible combinations to get i
        """
        dp = [1] + [0 for i in range(target)]
        for subTarget in range(1, target+1):
            for num in nums:
                if (subTarget-num >= 0) :
                    dp[subTarget] += dp[subTarget-num]
        return dp[-1]
            
        
        
    # # enumerate: too slow
    # def combinationSum4(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     return self.combination(nums, target, [], 0)
    # 
    # def combination(self, nums, target, current, result):
    #     if target == 0:
    #         # result.append(current)
    #         result += 1
    #     elif target < 0:
    #         return result
    #     else:
    #         for num in nums:
    #             result = self.combination(nums, target-num, current+[num], result)
    #     return result


print Solution().combinationSum4([1,2,3], 4)
print Solution().combinationSum4([3,2,1], 5)
print Solution().combinationSum4([4,2,1], 32)