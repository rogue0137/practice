# 198. House Robber
# https://leetcode.com/problems/house-robber/

# WWC SF Workthrough
# Do this solution and literally loop through everything in the comments
# this is the final version my group got to; you should reset the values from the first iteration
# HOUSE VALUES -> [1,2,3,1]
# OUTPUT = 4

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev_max_val = 0 # two house before current one's value
        prev_max_val = 0 # one house before current one's value
        curr_max_val = 0 # curr one's value
        # use float('inf') / float('-inf') if not all house values were positive

        for cur_house_val in nums: # house: 4 
            # cur_house_val = 1
            # STORE INFO FOR LATER
            temp_curr_max_val = curr_max_val # 4
            temp_prev_max_val = prev_max_val # 2
            
            # START RESETTING
            # prev_prev_max_val + cur_house_val = 1 + 1 = 2
            # prev_max_val + cur_house_val = 2 + 1 = 1
            curr_max_val =  max(prev_prev_max_val + cur_house_val, prev_max_val + cur_house_val)
            # curr_max_val = 2
            prev_max_val = temp_curr_max_val # 4
            prev_prev_max_val = temp_prev_max_val # 2 
            # pp: 2, p: 4, c: 2
            
            #FINISHED LOOPING: P: 4, C: 2
        return max(prev_max_val, curr_max_val)


## Annat's amazing solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_ago = 0
        one_house_ago = 0
        
        for i in range(len(nums)):
            rob_the_house = two_houses_ago + nums[i]
            skip_the_house = one_house_ago
            
            two_houses_ago = one_house_ago
            one_house_ago = max(rob_the_house, skip_the_house)
            
        
        return max(two_houses_ago, one_house_ago)


# With temp variables: these are more performant than the solution that using python non-temp variable magic
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev_max_val = 0
        prev_max_val = 0
        curr_max_val = 0

        # print(f'prev_prev_max_val: {prev_prev_max_val}')
        # print(f'prev_max_val: {prev_max_val}')
        # print(f'curr_max_val: {curr_max_val}')
        for cur_house_val in nums:
            # print(f'current house value: {cur_house_val}')
            temp_prev_max_val = prev_max_val
            temp_curr_max_val = curr_max_val
            curr_max_val =  max(
                prev_prev_max_val + cur_house_val, 
                prev_max_val +cur_house_val)
            prev_prev_max_val = temp_prev_max_val
            prev_max_val = temp_curr_max_val
            # print(f'prev_prev_max_val: {prev_prev_max_val}')
            # print(f'prev_max_val: {prev_max_val}')
            # print(f'curr_max_val: {curr_max_val}')
        return max(prev_max_val, curr_max_val)
# Runtime: 28 ms, faster than 80.75% of Python3 online submissions for House Robber.
# Memory Usage: 13.7 MB, less than 82.76% of Python3 online submissions for House Robber.

# Without temp variables
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev_max_val = prev_max_val = curr_max_val = 0
        for cur_house_val in nums:
            prev_prev_max_val, prev_max_val, curr_max_val = (
                prev_max_val, 
                curr_max_val, 
                max(prev_prev_max_val + cur_house_val, prev_max_val + cur_house_val))
        return max(prev_max_val, curr_max_val)
# Runtime: 32 ms, faster than 57.63% of Python3 online submissions for House Robber.
# Memory Usage: 13.8 MB, less than 73.59% of Python3 online submissions for House Robber.
