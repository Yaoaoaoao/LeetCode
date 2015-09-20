class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sum_ = 0
        for i in range(1, len(prices)):
            sum_ += max(0, prices[i] - prices[i-1])
        return sum_
    
        return sum([max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))])
    
    