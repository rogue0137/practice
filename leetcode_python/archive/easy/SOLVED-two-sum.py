# 1. Two Sum
# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()
        for i in range(len(nums)):
            num_one = nums[i]
            num_two = target - num_one
            if num_two in sum_dict:
                return [i, sum_dict[num_two]]
            else:
                sum_dict[num_one] = i

# Runtime: 80 ms, faster than 36.14% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 51.87% of Python3 online submissions for Two Sum.