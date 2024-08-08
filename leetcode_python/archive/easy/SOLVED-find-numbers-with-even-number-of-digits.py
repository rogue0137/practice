# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num_digits = 0
        for num in nums:
            len_of_num = len(str(num))
            if len_of_num % 2 == 0:
                even_num_digits += 1
        return even_num_digits

# Runtime: 48 ms, faster than 92.98% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 55.82% of Python3 online submissions for Find Numbers with Even Number of Digits.