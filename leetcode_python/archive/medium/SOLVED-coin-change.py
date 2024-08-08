# 322. Coin Change
# https://leetcode.com/problems/coin-change/

# use float('inf') when looking for min 
# use float('-inf') when looking for max
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        need = [0] + [amount + 1] * amount
        # print(f'need: {need}')
        for c in coins:
            # print(f'c: {c}')
            for a in range(c, amount+1):
                # print(f'a: {a}')
                # print(f'a-c:{a-c}')
                # print(f'need[a]: {need[a]}, need[a-c] + 1: {need[a-c] + 1}')
                need[a] = min(need[a], need[a - c] + 1)
                # print(f'updated need: {need}')
        if need[-1] <= amount:
            return need[-1]  
        else:
            return -1

tests = [
    dict(coins=[1, 2, 5], amount=11, answer=3),
    dict(coins=[2], amount=3, answer=-1)
]

for test in tests:
    new_solution = Solution()
    assert new_solution.coinChange(test['coins'], test['amount']) == test['answer']