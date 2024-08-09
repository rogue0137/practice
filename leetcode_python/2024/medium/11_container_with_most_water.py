# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # find two numbers that multipled equal the biggest surface

        left_index = 0
        right_index = len(height) - 1
        max_water = float('-inf')

        while left_index < right_index:
            # calculate the distance between two heights
            total_distance = right_index - left_index

            left_height = height[left_index]
            right_height = height[right_index]

            # The water area is determined by the shorter line (lower height) and the distance between the lines
            # So, we calculate the potential water area as the product of the lower height and the total distance
            # Then, move the pointer of the shorter line towards the center, hoping to find a taller line that increases the water area
            
            if left_height < right_height:
                curr_water = left_height * total_distance
                left_index += 1
            else:
                curr_water = right_height * total_distance
                right_index -= 1

            max_water = max(max_water, curr_water)


        return max_water
