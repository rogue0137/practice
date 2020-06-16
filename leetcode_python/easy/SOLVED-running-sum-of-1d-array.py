# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_array = []
        len_of_nums = len(nums)
        for i in range(1, len_of_nums + 1):
            add_to_array = sum(nums[:i])
            new_array.append(add_to_array)
        return new_array

# Runtime: 60 ms, faster than 59.38% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.2 MB, less than 33.33% of Python3 online submissions for Running Sum of 1d Array.