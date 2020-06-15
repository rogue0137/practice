# Write an efficient function that takes stock_prices_yesterday
# and returns the best profit I could have made from 1 purchase
# and 1 sale of 1 Apple stock yesterday.

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# actual solution


def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    print('starting min price: ' + str(min_price))
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    print('starting max profit: ' + str(max_profit))

    rounds = 1
    for index, current_price in enumerate(stock_prices_yesterday):
        print('Round ' + str(rounds))
        print('\t index: ' + str(index) + ', current price: ' + str(current_price) )
        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy *and* sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be *negative*--we'd return 0.
        if index == 0:
            rounds += 1
            continue


        # see what our profit would be if we bought at the
        # min price and sold at the current price

        potential_profit = current_price - min_price
        print('\t\t potential profit:' + str(potential_profit) + ' = ' +
              str(current_price) + ' - ' + str(min_price))

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        print('\t\t new max profit: ' + str(max_profit))

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)
        print('\t\t new min price: ' + str(min_price))

        rounds += 1

    return max_profit

profit = get_max_profit(stock_prices_yesterday)
print('Max profit is ' + str(profit))
# returns 6 (buying for $5 and selling for $11)
