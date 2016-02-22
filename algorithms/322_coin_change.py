class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_value = float("inf")
        dp = [0] + [max_value] * amount
        
        for i in range(1, amount+1):
            dp[i] = min([ dp[i-c] if i-c >=0 else max_value for c in coins]) + 1
        
        return dp[amount] if dp[amount] != max_value else -1
        
        
        
print Solution().coinChange([1, 2, 5], 11)
print Solution().coinChange([2], 3)