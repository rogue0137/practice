# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

# Two pointer approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        L = 0
        R = len(height) - 1
        while L < R:
            # area = L * W
            length = min(height[L], height[R])
            width = R - L
            curr_area = length * width
            max_area = max(max_area, curr_area)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return max_area

# Runtime: 240 ms, faster than 6.61% of Python3 online submissions for Container With Most Water.
# Memory Usage: 15.2 MB, less than 94.72% of Python3 online submissions for Container With Most Water.

