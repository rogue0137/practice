# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# WWC SF 6/29
# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # [ 1, 2, 3] array input
         # [ 1, 2] continguous subarray 
         # [ 1, 3] subarray, but not contiguous
         # 6 expected output
         # contiguous subarray sums:
         # 1, 2, 3 = 6
         # 1, 2 = 3
         # 2, 3 = 5
         
        # 1. access the length of the array
        arr_len = len(nums)
        # 2. final value -- DP here: we are "caching" a value and updating it
        max_sum = nums[0] # 1 
        # 3. intermediate value
        temp_sum = nums[0] # 1
        
        # 4. loop, range()
        for i in range(1, arr_len):
            num = nums[i] # 3 --> 2
            # 5. within loop, max or min 
            # 6. you'll usually have at least two of these
            # contiguous = either the number by itself is larger
            #   or all the numbers before it PLUS the number are larger
            
            # 7. start resetting for the next loop
            # reset the temp_sum: will change
            # reset the max_sum: may or may not change
            # max(3, 3 + 3 = 6) --> max(2, 1 + 2 = 3)
            # -- DP below: we are repeating a mathematical equation
            #.   to find out answer
            # MAX 1
            temp_sum = max(num, temp_sum + num) # 6 --> 3
            # MAX 2
            # max(6, 3) --> max(1, 3)
            max_sum = max(temp_sum, max_sum) # 6 --> 3
            


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