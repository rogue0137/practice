# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
# Runtime: 68 ms, faster than 8.51% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 57.18% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        starting_num = nums[0]
        prev_num = nums[0] 
        for num in nums[1:]:
            if prev_num > num:
                return num
            prev_num = num
        return starting_num
# Runtime: 44 ms, faster than 46.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 63.22% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

# Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # go through the array starting on the outside working in
        L, R = 0, len(nums) - 1
        while L < R:
            midpoint = (L + R) // 2
            if nums[midpoint] > nums[R]:
                # move L one to the right
                L = midpoint + 1
            else:
                # move R to the old midpoint to get closer to actual num
                R = midpoint
        return nums[L]
# Runtime: 52 ms, faster than 19.94% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.2 MB, less than 16.85% of Python3 online submissions for Find Minimum in Rotated Sorted Array.