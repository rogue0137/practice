# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_as_list = [int(x) for x in str(n)]
        prod_of_digits = 1
        for i in range(len(n_as_list)):
            prod_of_digits = prod_of_digits * n_as_list[i]
        sum_of_digits = sum(n_as_list)
        diff_btwn_prod_and_sum = prod_of_digits - sum_of_digits
        return diff_btwn_prod_and_sum

# Runtime: 32 ms, faster than 46.62% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.7 MB, less than 75.18% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.