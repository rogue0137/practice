# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# The idea of peaks/valleys, a.k.a. local_maximum and local_minum are key to using a
# Greedy Algorith to solve this question

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize maximum profit to 0 since we start with no transactions.
        max_profit = 0

        # Initialize current minimum price and current maximum price to the first day's price.
        curr_min_price = prices[0]
        curr_max_price = prices[0]

        # Iterate through the rest of the prices starting from the second day.
        for i in range(1, len(prices)):
            curr_price = prices[i]

            # Check if the current price is less than the current maximum price.
            # This indicates a potential dip in price, suggesting we might have reached a peak previously.
            if curr_price < curr_max_price:
                # Sell the stock before the price drops further.
                # Add the profit from the last buy-sell cycle to the total profit.
                max_profit += curr_max_price - curr_min_price

                # Update both the current minimum price and maximum price to the current price,
                # preparing for the next potential buy-sell cycle.
                curr_min_price = curr_price
                curr_max_price = curr_price
            else:
                # If the current price is higher than the current minimum price,
                # it means we might be at a new peak. Update the current maximum price.
                curr_max_price = curr_price

        # After the loop ends, ensure we sell the stock to capture any remaining profit.
        # This accounts for the scenario where the last day's price is the highest.
        max_profit += curr_max_price - curr_min_price

        # Return the total maximum profit achieved through all buy-sell cycles.
        return max_profit

# A greedy algorithm makes the locally optimal choice at each stage with the hope of finding a global optimum. 
# In the context of your solution, you're being "greedy"/making decisions based on the current state (prices) without considering 
# future states beyond what's necessary for the immediate decision.
