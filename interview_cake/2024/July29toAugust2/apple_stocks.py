# Writing programming interview questions hasn't made me rich yet ... 
# so I might give up and start trading Apple stocks all day instead.

# First, I wanna know how much money I could have made yesterday if I'd 
# been trading Apple stocks all day.

# So I grabbed Apple's stock prices from yesterday and put them in a 
# list called stock_prices, where:

# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

# Write an efficient function that takes stock_prices and returns the best profit I could 
# have made from one purchase and one sale of one share of Apple stock yesterday.

def get_max_profit(stock_prices):

    if len(stock_prices) <= 1:
        raise ValueError("You need at least two prices")
        
    # Using float('-inf') since there could be a negative profit
    max_profit = float('-inf')
    
    min_price = stock_prices[0]
    
    for new_price in stock_prices[1:]:
        max_profit = max(max_profit, new_price - min_price)
        min_price = min(min_price, new_price)
    

    return max_profit

# 0(N) time complexity since we loop through the list once
# 0(1) space complexity since our newly created space is not dependent on the size of N
