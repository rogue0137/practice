# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=dynamic-programming&difficulty=HARD

# This problem can also be solved via the following ways:
#   - brute force 
#   - two pointers
#   - stack based
# Below, it is solved using dynamic programming since that is the focus this week.

# This problem is a "fun" hybrid of using memoization and tabulation dynamic programming approaches.
#  - DP because the solution breaks down the problem into smaller subproblems
#  - memoization (storing results) 
#  - with iterative tabular computation (filling arrays)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: Check if the input list is empty or has only one element
        if not height or len(height) < 2:
            return 0

        array_length = len(height)
        
        # Initialize two arrays to store the maximum height to the left and right of each position
        max_height_left = [0] * array_length
        max_height_right = [0] * array_length
        
        # Calculate the maximum height to the left of each position
        max_height_left[0] = height[0]
        # Note that we are iterating forwards here
        for i in range(1, array_length):
            max_height_left[i] = max(max_height_left[i-1], height[i])
        
        # Calculate the maximum height to the right of each position
        max_height_right[array_length - 1] = height[array_length - 1]
        # Note that we are iterating backwards here
        for i in range(array_length - 2, -1, -1):
            max_height_right[i] = max(max_height_right[i+1], height[i])
        
        # Calculate the total trapped water
        total_trapped_water = 0

        for i in range(array_length):
            # The water trapped at each position is the minimum of the left and right max heights,
            # minus the height at the current position (if positive)
            water_at_position = min(max_height_left[i], max_height_right[i]) - height[i]
            if water_at_position > 0:
                total_trapped_water += water_at_position
        
        return total_trapped_water
