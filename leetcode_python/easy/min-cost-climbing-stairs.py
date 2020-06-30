# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List
# Come back and do memoization

# Recursive solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_of_cost = len(cost)
        return min(self.minCost(cost, len_of_cost - 1), self.minCost(cost, len_of_cost - 2))

    def minCost(self, cost:List[int], list_len: int) -> int:
        if list_len < 0:
            return 0
        if list_len == 0 or list_len == 1:
            return cost[list_len]
        return cost[list_len] + min(self.minCost(cost, list_len - 1) , self.minCost(cost, list_len - 2))


tests = [
    dict(cost=[10,15,20], output=15),
    dict(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], output=6),
    dict(cost=[0,1,1,0], output=1)
]

for test in tests:
    solution = Solution()
    assert solution.minCostClimbingStairs(test['cost']) == test['output']