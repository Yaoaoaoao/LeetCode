class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        buy, profit = prices[0], 0
        for i in prices:
            buy = min(buy, i)
            profit = max(profit, i-buy)
        return profit
    
print Solution().maxProfit([1]) #1
# print Solution().maxProfit([1,2]) #1
# print Solution().maxProfit([3,2,6,5,0,3]) #4