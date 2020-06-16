# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        new_list = []
        # if you sort the nums in order, you can count exactly how many nums are smaller by noting the index of the num!
        sorted_nums = sorted(nums)
        for index, num in enumerate(sorted_nums):
            # setdefault(key, value)
            # if you have the same number multiple times, it will not reset after the first time set, so you will always get the lowest index
            indices.setdefault(num, index)
        print(f'indices: {indices}')
        for num in nums:
            print(f'indices[num]:{indices[num]}')
            new_list.append(indices[num])
        return new_list


# Runtime: 76 ms, faster than 68.27% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14 MB, less than 15.54% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.