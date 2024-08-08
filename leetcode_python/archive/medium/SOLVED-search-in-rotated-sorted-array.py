# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            midpoint = (L + R) // 2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] > nums[R]:
                if nums[L] <= target and target < nums[midpoint]:
                    R = midpoint - 1
                else:
                    L = midpoint + 1
            else:
                if nums[midpoint] < target and target <= nums[R]:
                    L = midpoint + 1
                else:
                    R = midpoint - 1
        return -1
# Runtime: 64 ms, faster than 11.96% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 66.13% of Python3 online submissions for Search in Rotated Sorted Array.