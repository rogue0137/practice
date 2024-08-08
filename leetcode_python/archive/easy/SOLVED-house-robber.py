# 198. House Robber
# https://leetcode.com/problems/house-robber/

# WWC SF Workthrough 7/9
# https://leetcode.com/problems/house-robber/submissions/
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. access the length of the array
        len_arr = len(nums) # 4
        # 2. potential final value 1
        max_val_two_houses_ago = 0
        # 3. potential final value 2
        max_val_one_house_ago = 0
                    
        # 4. loop
        for i in range(len_arr): 
            cur_house_val = nums[i] # 1 --> 3 --> 2 --> 1
​
            # 5. within loop, max or min: MAX here 
            # 6. you'll usually have at least two of these
            # -- DP below: we are repeating a mathematical equation
            #    to find out answer
            
            # 1 + 1 --> 1 + 3 --> 0 + 2 --> 0 + 1
            rob_cur_house = max_val_two_houses_ago + cur_house_val
            # 4 --> 1 --> 1 --> 0
            skip_cur_house = max_val_one_house_ago
            
            # 7. start resetting for the next loop
            max_val_two_houses_ago = max_val_one_house_ago # 4 --> 1 --> 1 --> 0
            # MAX 1
            # max(2, 4) --> max(4, 1) --> max(2, 1) --> max(1, 0)
            max_val_one_house_ago = max(rob_cur_house, skip_cur_house) # 4 --> 4 --> 2 --> 1
            
            
        # MAX 2
        # max(4, 4)



# WWC SF Workthrough 6/25
# Do this solution and literally loop through everything in the comments
# this is the final version my group got to; you should reset the values from the first iteration
# HOUSE VALUES -> [1,2,3,1]
# OUTPUT = 4

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev_max_val = 0 # two house before current one's value
        prev_max_val = 0 # one house before current one's value
        curr_max_val = 0 # curr one's value
        # ?:use float('inf') / float('-inf') if not all house values were positive

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
