# 136. Single Number
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        len_of_nums = len(nums)
        for i in range(0, len_of_nums, 2):
            if i == len_of_nums - 1:
                return sorted_nums[i]
            if sorted_nums[i] != sorted_nums[i+1]:
                return sorted_nums[i]

# Runtime: 88 ms, faster than 70.69% of Python3 online submissions for Single Number.
# Memory Usage: 16.3 MB, less than 69.36% of Python3 online submissions for Single Number.
