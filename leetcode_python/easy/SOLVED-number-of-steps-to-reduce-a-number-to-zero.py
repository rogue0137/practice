# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps_counter = 0
        while num != 0:
            steps_counter += 1
            if num % 2 == 0:
                num = int(num / 2)
            else:
                num -= 1
        return steps_counter

# Runtime: 20 ms, faster than 98.41% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 40.46% of Python3 online submissions for Number of Steps