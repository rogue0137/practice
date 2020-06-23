# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# DYNAMIC PROGRAMMING, RECURSION -- DOES NOT WORK ON LEETCODE, NOR LOCAL COMP
# Cannot work because of Python's poor implementation of tail-call elmination
# https://en.wikipedia.org/wiki/Tail_call
# changing the system recursion limits was useless
import sys
sys.getrecursionlimit() # 1000 for me
sys.setrecursionlimit(34500) # still get: RecursionError: maximum recursion depth exceeded in comparison
sys.setrecursionlimit(35500) # get: segmentation fault

def maxSubArray(nums):
    l_nums = len(nums)
    # base case
    if l_nums == 1:
        return nums[0]
    # dynamic/recursive case broken out
    L = nums[:l_nums]
    R = nums[l_nums:]
    LSum = maxSubArray(L)
    RSum = maxSubArray(R)
    return max(LSum,RSum)
    # instead of lines 19 - 23, could also do the following in one go:
    # return max(maxSubArray(nums[:l_nums], maxSubArray(nums[l_nums:])))

assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert maxSubArray([6,2,2,3]) == 9


# DYNAMIC PROGRAMMING, NO RECURSION -- PASSES LEETCODE
# because you can't use recursion for most python solutions, you need to
# keep track of variables; they will usually be a cur_var and max_var of some sort
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, len_of_nums):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum

# Runtime: 72 ms, faster than 45.96% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.5 MB, less than 64.53% of Python3 online submissions for Maximum Subarray.