# 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_product = (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)
        return max_product

# Runtime: 56 ms, faster than 60.42% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 13.9 MB, less than 39.89% of Python3 online submissions for Maximum Product of Two Elements in an Array.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num_one = max(nums)
        index_one = nums.index(max(nums))
        del nums[index_one]
        num_two = max(nums)
        index_two = nums.index(max(nums))
        max_product = (num_one - 1) * (num_two - 1)
        return max_product

# faster and more memory efficient
# Runtime: 40 ms, faster than 99.48% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Memory Usage: 13.8 MB, less than 62.67% of Python3 online submissions for Maximum Product of Two Elements in an Array.
# Ne