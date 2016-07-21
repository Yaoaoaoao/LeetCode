class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Standard dfs methods. n!
        numberLeft, remain, current, combine, result = k, n, 0, [], []
        return self.combinationSum(numberLeft, remain, current, combine, result)
        
    def combinationSum(self, numberLeft, remain, current, combine, result):
        if numberLeft == 0:
            if remain == 0:
                result.append(combine)
        else:
            for i in range(current+1, min(10, remain+1)):
                if (remain-i) < 0: 
                    continue
                self.combinationSum(numberLeft-1, remain-i, i, combine+[i], result)
        return result

print Solution().combinationSum3(3, 7)
print Solution().combinationSum3(3, 9)
print Solution().combinationSum3(2, 18)
