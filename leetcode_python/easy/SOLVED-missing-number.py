# 268. Missing Number
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        list_with_missing_num = range(0,len_of_nums + 1)
        for num in list_with_missing_num:
            if num not in nums:
                return num

# Runtime: 5536 ms, faster than 5.02% of Python3 online submissions for Missing Number.
# Memory Usage: 15.1 MB, less than 42.17% of Python3 online submissions for Missing Number.