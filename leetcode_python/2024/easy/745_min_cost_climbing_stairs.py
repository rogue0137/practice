# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM,EASY&status=SOLVED

from typing import List

# DP often uses memoization. 
# cost_two_steps_back and cost_one_step_back are memoized values.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_of_cost = len(cost)
        
        # Edge case: you need at least 2 indexes to start at index 1
        if len_of_cost < 2:
            return 0
        
        # Initialize our "memoized" values
        # cost_two_steps_back stores the minimum cost to reach the second-to-last step
        # cost_one_step_back stores the minimum cost to reach the last step
        cost_two_steps_back = cost[0]
        cost_one_step_back = cost[1]
        
        # Now, we fill in the rest of our "memoized" values
        for i in range(2, len_of_cost):
            # Calculate the current cost to reach this step
            current_cost = cost[i] + min(cost_one_step_back, cost_two_steps_back)
            
            # Update our "memoized" values for the next two steps
            cost_two_steps_back = cost_one_step_back
            cost_one_step_back = current_cost
        
        # Return the minimum cost between the last two steps
        return min(cost_one_step_back, cost_two_steps_back)
