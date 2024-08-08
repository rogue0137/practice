# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

# More memory efficient, using 3 variables
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        num_1 = 0
        num_2 = 0
        num_3 = 1 
        print(f'starting nums: num1: {num_1}, num2: {num_2}, num3:{num_3}')
        for i in range(3, n):
            print('in loop')
            cur_num = num_1 + num_2 + num_3
            num_3 = num_2
            num_2 = num_1
            num_1 = curr_num
            print(f'last mums: num1: {num_1}, num2: {num_2}, num3:{num_3}')
        return num_1 + num_2 + num_3

# Less memory efficient (using cache)
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         # sum of T at n index
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         # python always starts at 0 index, so to get something at index X
#         # you'll have to add 1 to X
#         cache = [0] * (n + 1)
#         # tribinacci sequence starts 0, 0, 1
#         cache[2] = 1
#         # only continue to here if the n is 3 or greater
#         if n > 2:
#             for i in range(3, n + 1):
#                 # this updates the number at N index
#                 cache[i] = cache[i-3] + cache[i-2] + cache[i-1]
#                 # print(f'cache: {cache}')
#         # remember that you're looking for the sum of the last three numbers
#         # in the sequence, starting with index n
#         return sum(cache[-3:])

# Runtime: 32 ms, faster than 45.96% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 33.75% of Python3 online submissions for N-th Tribonacci Number.

tests = [
    dict(n=2, output=1),
    dict(n=3, output=2),
    dict(n=4, output=4),
    dict(n=5, output=7),
    dict(n=25, output=1389537),
    dict(n=1, output=1)
]

for test in tests:
    solution = Solution()
    print(solution.tribonacci(test['n']))
    assert solution.tribonacci(test['n']) == test['output']