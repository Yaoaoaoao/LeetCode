class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy, profit = prices[0], 0
        buy2, profit2 = prices[0], 0
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p - buy)
            buy2 = min(buy2, p - profit)
            profit2 = max(profit2, p-buy2)
        return profit2