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