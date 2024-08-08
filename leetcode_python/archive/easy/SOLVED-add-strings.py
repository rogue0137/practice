# https://leetcode.com/problems/add-strings/
# 415. Add Strings

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_as_int = int(num1)
        num2_as_int = int(num2)
        sum_of_nums = num1_as_int + num2_as_int
        str_sum_of_nums = str(sum_of_nums)
        return str_sum_of_nums

# Runtime: 32 ms, faster than 94.64% of Python3 online submissions for Add Strings.
# Memory Usage: 14.1 MB, less than 24.65% of Python3 online submissions for Add Strings.