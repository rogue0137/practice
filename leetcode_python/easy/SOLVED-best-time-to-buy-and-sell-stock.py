# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            curr_max_profit = sell - min_buy
            max_profit = max(max_profit, curr_max_profit)
            min_buy = min(min_buy, sell)
        return max_profit

# Runtime: 84 ms, faster than 21.86% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15.2 MB, less than 43.23% of Python3 online submissions for Best Time to Buy and Sell Stock.