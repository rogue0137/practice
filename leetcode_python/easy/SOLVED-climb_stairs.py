# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# Dynamic Programming
# 1. Find base case
# 2. Find dynamic case


# Memoized Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        cache = [1] * n
        for i in range(1, n):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[-1]
# Runtime: 32 ms, faster than 44.53% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 39.76% of Python3 online submissions for Climbing Stairs.

# Recursive solution
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return (self.climbStairs(n-1) + self.climbStairs(n-2))
# This solution breaks leetcode, but works locally.

tests = [
    dict(input=2, output=2),
    dict(input=3, output=3),
    dict(input=7, output=21)
]

for test in tests:
    solution = Solution()
    assert solution.climbStairs(test['input']) == test['output']
