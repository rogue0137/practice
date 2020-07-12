# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        int_to_str = '{0:b}'.format(n)
        replace_zeros = int_to_str.replace('0','')
        list_of_ones = list(replace_zeros)
        num_of_ones = len(list_of_ones)
        return num_of_ones

# Runtime: 44 ms, faster than 16.03% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14 MB, less than 16.74% of Python3 online submissions for Number of 1 Bits.