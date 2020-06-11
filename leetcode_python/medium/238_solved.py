# 238. Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/
# trick: use right and left sides

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_of_nums = len(nums)
        nums_products = [0] * len_of_nums
        # nothing to the left of position 1
        nums_products[0] = 1
        for i in range(1, len_of_nums):
            # fill from left first
            print(f'nums_products: {nums_products}')
            print(f'nums[i-1]: {nums[i-1]}')
            print(f'nums_products[i - 1]: {nums_products[i - 1]}')
            nums_products[i] = nums[i - 1] * nums_products[i - 1]
        # fill from right
        print(f'nums_products: {nums_products}')
        right_side_product = 1
        reversed_len = reversed(range(len_of_nums))
        print(f'reversed_len: {reversed_len}')
        for i in reversed_len:
            nums_products[i] = nums_products[i] * right_side_product
            right_side_product *= nums[i]
            print(f'right_side_product: {right_side_product}')
        return nums_products

# Below without comments and prints
# Runtime: 112 ms, faster than 97.77% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.5 MB, less than 62.87% of Python3 online submissions for Product of Array Except Self.