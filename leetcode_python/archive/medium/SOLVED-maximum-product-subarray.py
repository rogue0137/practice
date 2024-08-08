# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

# DP Approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        max_prod = nums[0]
        for num in nums[1:]:
            # you need to see which is bigger, two negative numbers
            # (potentially prev_min * num) can give a bigger product
            max_num_plus = max(prev_max * num, prev_min * num) 
            min_num_plus = min(prev_max * num, prev_min * num)
            # get currents
            curr_max = max(max_num_plus, num)
            curr_min = min(min_num_plus, num)
            max_prod = max(max_prod, curr_max)
            # set current to prev for next loop
            prev_max = curr_max
            prev_min = curr_min
        return max_prod

# Runtime: 96 ms, faster than 9.26% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 13.9 MB, less than 83.38% of Python3 online submissions for Maximum Product Subarray.

# Linear Approach
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        # set curr_prod
        curr_prod = 1

        for num in nums:
            curr_prod *= num
            max_prod = max(curr_prod, max_prod)
            if curr_prod == 0:
                curr_prod = 1

        # reset curr_prod
        curr_prod = 1

        for num in reversed(nums):
            curr_prod *= num
            max_prod = max(curr_prod, max_prod)
            if curr_prod == 0:
                curr_prod = 1
        return max_prod

# Runtime: 92 ms, faster than 11.05% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14 MB, less than 78.53% of Python3 online submissions for Maximum Product Subarray.