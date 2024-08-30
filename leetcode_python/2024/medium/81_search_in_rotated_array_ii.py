# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/


from typing import List

class Solution:
    def search(nums, target):

        # Your basic "check the thing exists" check
        if not nums:
            return False
        
        left_index, right_index = 0, len(nums) - 1
        
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_element = nums[middle_index]
            
            # Check if the middle element matches the target
            if middle_element == target:
                return True
            
            left_boundary = nums[left_index]
            right_boundary = nums[right_index]

            # Check if we're in the rotated OR non-rotated/sorted portion of the array
            # NOTE: Because of duplicates, it's possible to NOT know. We usually have an easy if/else
            # for rotated arrays; because of duplicates we now have a third scenario, so need the
            # if/elif/else pattern
            # ANOTHER NOTE: You can also solve it by checking if the left half or right half is sorted.
            # That was less intuitive to me than checking rotated vs. non-rotated half because of the
            # way I've been studying, but do what works for you!

            # We're in the rotated portion
            if left_boundary > middle_element:
                # Target could be in the rotated portion
                if middle_element < target <= right_boundary:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index - 1
            # We're in the unrotated portion
            elif left_boundary < middle_element:
                # Target could be in the unrotated portion
                if left_boundary <= target < middle_element:
                    right_index = middle_index - 1
                else:
                    left_index = middle_index + 1
            # We can't determine which portion we're in due to duplicates
            else:
                # Move the left pointer one step at a time
                left_index += 1
        return False


# SHOWING WORK USING EXAMPLE CASES

# EXAMPLE 1:
# nums = [2,5,6,0,0,1,2]
# target = 0
# Expected output: True
# Initial setup
#   left_index, right_index = 0, 6
# LOOP 1
# left_index = 0, right_index = 6
    # middle_index = (0 + 6) // 2 = 3
    # middle_element = nums[3] = 0
    # Check if middle element matches target
    # middle_element == target  # True
    # Target found, return True

# EXAMPLE 2:
# nums = [2,5,6,0,0,1,2]
# target = 3
# Expected output: False
# Initial setup
#   left_index, right_index = 0, 6
# LOOP 1
# left_index = 0, right_index = 6
    # middle_index = (0 + 6) // 2 = 3
    # middle_element = nums[3] = 0
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[0] = 2
    # right_boundary = nums[6] = 2
    # 2 > 0, so we're in the rotated portion
    # 0 < 3 <= 2 is false, so right_index = middle_index - 1 = 2
# LOOP 2
# left_index = 0, right_index = 2
    # middle_index = (0 + 2) // 2 = 1
    # middle_element = nums[1] = 5
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[0] = 2
    # right_boundary = nums[2] = 6
    # 2 < 5, so we're in the unrotated portion
    # 2 <= 3 < 5 is true, so right_index = middle_index - 1 = 0
# LOOP 3
# left_index = 0, right_index = 0
    # middle_index = (0 + 0) // 2 = 0
    # middle_element = nums[0] = 2
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[0] = 2
    # right_boundary = nums[0] = 2
    # 2 == 2, so we can't determine which portion we're in
    # left_index += 1 = 1
# Loop ends because left_index > right_index
# Return False

# EXAMPLE 3:
# nums = [3,1,2,3,3,3,3]
# target = 2
# Expected output: True
# Initial setup
#   left_index, right_index = 0, 6
# LOOP 1
# left_index = 0, right_index = 6
    # middle_index = (0 + 6) // 2 = 3
    # middle_element = nums[3] = 3
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[0] = 3
    # right_boundary = nums[6] = 3
    # 3 == 3, so we can't determine which portion we're in
    # left_index += 1 = 1
# LOOP 2
# left_index = 1, right_index = 6
    # middle_index = (1 + 6) // 2 = 3
    # middle_element = nums[3] = 3
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[1] = 1
    # right_boundary = nums[6] = 3
    # 1 < 3, so we're in the unrotated portion
    # 1 <= 2 < 3 is true, so right_index = middle_index - 1 = 2
# LOOP 3
# left_index = 1, right_index = 2
    # middle_index = (1 + 2) // 2 = 1
    # middle_element = nums[1] = 1
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[1] = 1
    # right_boundary = nums[2] = 2
    # 1 < 1 is false, 1 == 1 is true, so we can't determine which portion we're in
    # left_index += 1 = 2
# LOOP 4
# left_index = 2, right_index = 2
    # middle_index = (2 + 2) // 2 = 2
    # middle_element = nums[2] = 2
    # Check if middle element matches target
    # middle_element == target  # True
    # Target found, return True

# EXAMPLE 4:
# nums = [1]
# target = 0
# Expected output: False
# Initial setup
#   left_index, right_index = 0, 0
# LOOP 1
# left_index = 0, right_index = 0
    # middle_index = (0 + 0) // 2 = 0
    # middle_element = nums[0] = 1
    # Check if middle element matches target
    # middle_element == target  # False
    # left_boundary = nums[0] = 1
    # right_boundary = nums[0] = 1
    # 1 == 1, so we can't determine which portion we're in
    # left_index += 1 = 1
# Loop ends because left_index > right_index
# Return False
