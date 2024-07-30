# Write an efficient function that takes stock_prices_yesterday
# and returns the best profit I could have made from 1 purchase
# and 1 sale of 1 Apple stock yesterday.

# my solution
def get_max_profit(list_of_prices):
   return max(list_of_prices) - min(list_of_prices)

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

profit = get_max_profit(stock_prices_yesterday)
print(profit)
# returns 6 (buying for $5 and selling for $11)

