# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        integer_dict = dict()
        for num in nums:
            if num in integer_dict:
                return True
            else:
                integer_dict[num] = 1
        return False


# Runtime: 128 ms, faster than 64.62% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20 MB, less than 29.26% of Python3 online submissions for Contains Duplicate.