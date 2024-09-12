# https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=dynamic-programming&difficulty=MEDIUM&status=ATTEMPTED


# Dynamic Programming Basics
# - There are vairious types of problems. All DP require you to "save" values.
# - Sometimes you "save" using memoization. Sometimes you save using other strategies.
# - This is an example of using Tablation

# Memoization vs. Tabulation:

### Memoization ############################################################################
# Definition
# - Technique for optimizing performance by storing the results of expensive function calls
# - Avoids redundant computation by caching and reusing previously computed results

## Common Implementations
# - Top-down approach (often used with recursion)
# - Bottom-up approach (can be iterative), practice/leetcode_python/2024/medium/311_house_robber_iii.py is an example of this
# - Uses recursion (common in top-down implementations)
# - Can be implemented iteratively (bottom-up approach)

## Typical Data Structures
# - Hash tables (dictionaries in Python)
# - Arrays (for tabulation-style solutions)

## Key Characteristics
# - Reduces computational complexity by avoiding redundant calculations
# - Improves performance by leveraging pre-computed results
# - Useful for problems with overlapping subproblems

### Tabulation ############################################################################
# Tabulation
## Definition
# - Bottom-up approach to solving dynamic programming problems
# - Builds solutions to subproblems incrementally and stores them in a table
# - Used for problems where the optimal solution depends on solutions of subproblems

## Key Characteristics
# - Iterative approach (uses loops instead of recursion)
# - Constructs a table of solutions to subproblems
# - Solves all related subproblems in advance
# - Often more efficient than memoization for certain types of problems

## Typical Implementation
# - Uses a one-dimensional or multidimensional array to store solutions
# - Fills the table row by row (or layer by layer for multidimensional problems)
# - Usually involves nested loops to iterate over problem dimensions

## Advantages
# - Generally more efficient than memoization for problems with many overlapping subproblems
# - Avoids potential stack overflow issues associated with deep recursion
# - Provides a clear visual representation of problem-solving process

## Examples
# - Fibonacci sequence
# - Longest Increasing Subsequence
# - Coin Change Problem (this problem!!)
# - Knapsack Problem

## When to Use
# - Problems with optimal substructure property
# - Problems with overlapping subproblems
# - When dealing with large problem sizes that could cause stack overflow with recursive approaches

# Steps to Recognize Tabulation
# - Identify the problem as having optimal substructure and overlapping subproblems.
#   - Coin Change
#       - The problem asks for the minimum number of coins needed to reach a certain amount.
#       - The optimal solution for a larger amount often depends on the optimal solutions for smaller amounts.
#       - The problem likely involves calculating the minimum coins needed for various amounts. These calculations 
#         may overlap, as you'll need to consider the same subproblems repeatedly.
# - Realize that this type of problem is well-suited for dynamic programming.
# - Consider that an iterative approach (tabulation) is likely more efficient than recursion for large inputs.
# - Visualize how a table could be constructed to store solutions to subproblems.
# - Understand that filling this table iteratively, starting from base cases (amount 0), would solve the problem efficiently.


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Begin with Tabulation, a.k.a. an array, a.k.a. SET UP THE DP TABLE
        #   - We are using amount + 1 because we need to account for all possible amounts from 0 to the target amount
        #   - Initializing with float('inf') gives us enough space to represent the minimum number of coins for each amount
        #   - Using float('inf') also simplifies boundary conditions and loop iterations, for instance, min(float('inf'), SOMETHING ELSE)
        #     should always pick SOMETHING ELSE (unless you're comparing two float('inf'))

        # Here's an example:
        #    amount = 3
        #    dp = [4] * 4  # [4, 4, 4, 4]
        # After processing amount 0
        # dp = [0, 4, 4, 4] 
        # After processing amount 1
        # dp = [0, 1, 4, 4]
        # After processing amount 2
        # dp = [0, 1, 2, 4]
        # Final result after processing amount 3
        # dp = [0, 1, 2, 3]
        # Note that the above does not account for the coins part yet
        # You could also write below like:
        dp = [float('inf')] * (amount + 1)
        
        # Most DP problems start with Base Case of 0 to avoid division by zero problems within the for loop
        # We would not have division by zero problems for this specific case, however, in trying to train myself
        # to think in patterns common to types of problems, I am starting it as I would most other problems, hence
        # dp[0] = 0
        dp[0] = 0
        
        # Iterate through all amounts from 1 to target amount since we set dp[0] above
        for i in range(1, amount + 1):
            # For each coin, check if it can contribute to the current amount
            for coin in coins:
                if coin <= i:
                    # Calculate the potential number of coins if we use this coin
                    new_value = dp[i - coin] + 1
                    
                    # Compare the new potential solution with the current best known solution
                    # We only update if the new solution is better (fewer coins)
                    dp[i] = min(dp[i], new_value)
                    
                    # I'm leaving print statements here so you can walk through problems using it.
                    # It's super helpful in figuring out why he heck we need to loop through all the coins
                    # print(f'For i = {i}, checking coin {coin}')
                    # print(f'Current amount: {i}')
                    # print(f'Coin value: {coin}')
                    # print(f'Remaining amount after using this coin: {i - coin}')
                    # print(f'dp[{i}] before: {dp[i]}')
                    # print(f'dp[{i - coin}] + 1: {dp[i - coin] + 1}')
                    # print(f'New value: {new_value}')
                    # print(f'Updated dp[{i}]: {min(dp[i], new_value)}')
                    # print()

        
        # When using Tabulation, your answer will be at dp[amount]
        # If dp[amount] is still equal to the number you set it at the beginning, in our case float('inf'),
        # it was impossible to make that amount.
        if dp[amount] == float('inf'):
            return -1 
        return dp[amount]
