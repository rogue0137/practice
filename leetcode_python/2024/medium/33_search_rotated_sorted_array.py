# https://leetcode.com/problems/search-in-rotated-sorted-array/description/



# In order to get this problem right, you have to understand the concept of HOW we can find 
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # General properties of Binary Search:
        #   left/low
        #   right/high
        #   while loop, usually <=, sometimes <
        #   midpoint
        #   reset left/low or right/high -/+ exclusive
        left_index, right_index = 0, len(nums) - 1
        
        # Since the array may be rotated, we use <= in the while loop condition
        # to ensure we cover cases where the target is at the pivot or boundaries
        while left_index <= right_index:
            midpoint_index = (left_index + right_index) // 2
            midpoint_number = nums[midpoint_index]
            
            if midpoint_number == target:
                return midpoint_index
            
            # This is incredibly verbose, but I like very specific variable names, you could also use
            # left_boundary for number_to_the_left_of_the_midpoint_index and right_boundary for
            # number_to_the_right_of_the_midpoint_index = nums[right_index]
            number_to_the_left_of_the_midpoint_index = nums[left_index]
            number_to_the_right_of_the_midpoint_index = nums[right_index]

            # Determine which part of the array is sorted based on the relationship
            # between the left boundary, midpoint, and right boundary values.

            # Left half of the array is sorted
            if number_to_the_left_of_the_midpoint_index <= midpoint_number:
                # Example scenario: nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4], target = 7
                #   In an iteration, if left_index = 0 (nums[0] = 5), right_index = 9 (nums[9] = 4),
                #   and midpoint_index = 4 (nums[4] = 9):
                #   we have 5 <= 9.

                # If the target lies within this sorted portion, narrow the search to the left half.
                if number_to_the_left_of_the_midpoint_index <= target < midpoint_number:
                    right_index = midpoint_index - 1
                else:
                    # If the target does not lie in the sorted left half,
                    # it must be in the rotated part of the array, so we narrow the search to the right half.
                    left_index = midpoint_index + 1
            # Right side of the array is sorted
            else:
                # Example scenario: nums = [6, 7, 8, 1, 2, 3, 4, 5], target = 3
                #   If left_index = 0 (nums[0] = 6), right_index = 7 (nums[7] = 5),
                #   and midpoint_index = 3 (nums[3] = 1): 
                #   we have 6 > 1, indicating the right half is sorted.

                # If the target lies within this sorted portion, narrow the search to the right half.
                if midpoint_number < target <= number_to_the_right_of_the_midpoint_index:
                    left_index = midpoint_index + 1
                else:
                    # If the target does not lie in the sorted right half,
                    # it must be in the rotated part of the array, so we narrow the search to the left half.
                    right_index = midpoint_index - 1
        
        # Loop completed! Not in array
        return -1

