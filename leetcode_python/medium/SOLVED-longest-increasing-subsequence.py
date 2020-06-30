# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
# class Solution:
#     def lengthOfLIS(self, nums):
#         if not nums:
#             return 0
#         array_of_all_subsequences = []
#         len_of_nums = len(nums)
#         # for every num
#         for i in range(len_of_nums):
#             # get all their subsequences
#             # num_plus full name is curr_num_plus_all_increasing_numbers_that_follow_and_continue_to_increase
#             num_plus = [ nums[i] ]
#             highest_num = float('-inf')
#             for j in range(i, len_of_nums):
#                 if nums[j] > nums[i]:
#                     print(f'nums[j]: {nums[j]}, nums[i]: {nums[i]}')
#                     if nums[j] > highest_num:
#                         highest_num = nums[j]
#                         num_plus.append(highest_num)
#             array_of_all_subsequences.append(num_plus)
#         # get max of array of all subsequences
#         max_lis = max(array_of_all_subsequences, key=lambda x: len(x))# e.g if caching array [1, 2, 5, 4], output is 5
#         len_max_lis = len(max_lis)
#         return len_max_lis

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # array to check how many numbers before number at that index
        # are bigger than number [3,1,2,9] for "3", it would be 2
        number_subsequences_from_i = [1] * n #initialize with bunch of 1's

        #start at index 1....
        for i in range(1, n):
            # for i = 3, j would be 0, 1, 2
            # for i = 4, j would be 0, 1, 2,3
            
            #... now for that number, generate the subsequences
            #starter: [10,9,2,5,3,4]
            # if i is 2....
            #   number_subsequences_from_i[2] = 1 , from initialized
            #   is 10 > than 9
                #if so, then number_subsequences_from_i[2] is
                #number_subsequences_from_i[2] e.g. [9]
                #number_subsequences_from_i[1] + 1 (because ) [10,9]
            for j in range(0,i):
                
                #if 
                if nums[i] > nums[j]:
                    # why plus 1?
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
# Runtime: 1228 ms, faster than 34.37% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14 MB, less than 68.62% of Python3 online submissions for Longest Increasing Subsequence.

#In mathematics, a subsequence is a sequence that can be derived
# from another sequence by deleting some or no elements without changing the order of the remaining elements.

tests = [
    dict(input=[1,2,3], answer=3),
    dict(input=[10,9,2,5,3,7,101,18], answer=4),
    dict(input=[-2,-1], answer=2),
    dict(input=[10,9,2,5,3,4], answer=3)
]

for test in tests:
    new_solution = Solution()
    assert new_solution.lengthOfLIS(test['input']) == test['answer']