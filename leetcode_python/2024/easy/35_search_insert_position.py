# https://leetcode.com/problems/search-insert-position/description/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # left/low
        low = 0
        # right/high
        high = len(nums) - 1


        # while loop, usually <=, sometimes <
        while low <= high:
            # midpoint  
            midpoint = (low + high) // 2
            midpoint_num = nums[midpoint]

            if midpoint_num == target:
                return midpoint
            # reset low 
            elif midpoint_num < target:
                # add 1 so that it's exclusive of the midpoint
                low = midpoint + 1
            # reset high:
            else: 
                # minus 1 so that it's exclusive of the midpoint
                high = midpoint - 1
        
        # Your loop completed without finding the target value.
        # Why is low the answer? Three potential reasons.
        # 1. If your target is smaller than all numbers in nums
            # Original information: Array: [4, 6, 8, 10] Target: 3
            # Start loop:
                # Initial low = 0, high = 3.
                # Mid = 1 (value 6).
                # Target (3) < Mid (6), so high = mid - 1 = 0.
                # Now low = 0, high = 0, and the loop ends.
            # Target, if inserted, should be at low, 0.
        # 2. If your target is bigger than all numbers in nums
            # Original information: Array: [4, 6, 8, 10] Target: 11
            # Start loop:
                # Loop 1
                    # low = 0, high = 3.
                    # Calculate mid: (low + high) / 2 = (0 + 3) / 2 = 1
                    # nums[mid] = nums[1] = 6
                    # Since 11 > 6, the target is in the right half of the current search space.
                    # Update low: low = mid + 1 = 2
                # Loop 2
                    # low = 2, high = 3
                    # Calculate new mid: (low + high) / 2 = (2 + 3) / 2 = 2
                    # nums[mid] = nums[2] = 8
                    # Since 11 > 8, the target is still in the right half.
                    # Update low: low = mid + 1 = 3
                # Loop 3
                    # low = 3, high = 3
                    # Calculate new mid: (low + high) / 2 = (3 + 3) / 2 = 3
                    # nums[mid] = nums[3] = 10
                    # Since 11 > 10, the target is still in the right half.
                    # Attempt to update low: low = mid + 1 = 4. 
                    # However, since mid is already at the highest index, low moves beyond 
                    # the end of the array. The loop will end because low is greater than high.
                # Target, if inserted, should be at low, 4
        # 3. If your target is in between two numbers in nums
            # Original information: Array: [4, 6, 8, 10] Target: 7
            # Start loop
                # Loop 1
                    # low = 0, high = 3.
                    # mid: (low + high) / 2 = (0 + 3) / 2 = 1
                    # nums[mid] = nums[1] = 6
                    # Since 7 > 6, the target is in the right half of the current search space.
                    # Update low: low = mid + 1 = 2
                # Loop 2
                    # low = 2, high = 3
                    # Calculate new mid: (low + high) / 2 = (2 + 3) / 2 = 2
                    # nums[mid] = nums[2] = 8
                    # Since 7 < 8, the target is in the left half of the current search space.
                    # Update high: high = mid - 1 = 1
                    # low (2) is now greater than high (1), so the loop will end
                # Target, if inserted, should be at low, 2
        return low
            

                