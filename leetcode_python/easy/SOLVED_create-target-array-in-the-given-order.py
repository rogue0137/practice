# 1389. Create Target Array in the Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        len_of_nums = len(nums)
        new_nums_list = []
        for i in range(len_of_nums):
            val = nums[i]
            idx = index[i]
            new_nums_list.insert(idx, val)
        
        return new_nums_list

# Runtime: 32 ms, faster than 71.26% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.8 MB, less than 54.80% of Python3 online submissions for Create Target Array in the Given Order.

# changing for loop to only: new_nums_list.insert(index[i], nums[i])
# more memory, much faster

# Runtime: 28 ms, faster than 89.94% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.9 MB, less than 40.39% of Python3 online submissions for Create Target Array in the Given Order.