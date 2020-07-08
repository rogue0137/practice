# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

# using XOR BORE
class Solution:
    def getSum(self, a: int, b: int) -> int:
        abs_a, abs_b = abs(a), abs(b)
        if abs_a < abs_b:
            return self.getSum(b, a)
        # will the final number be a positive or negative integer
        sign = 1 if a > 0 else -1

        # check for negative integers
        if a * b >= 0:
            # while bits remain
            while abs_b:
                # x ^ y: what bits are diff between x and y
                # (x & y): which bits are the same
                # << 1: shift each bit left one
                abs_a, abs_b = abs_a ^ abs_b, (abs_a & abs_b) << 1
        else:
            # while bits remain
            while abs_b:
                # x ^ y: what bits are diff between x and y
                # ~x: add 1 to x, then change the sign
                abs_a, abs_b = abs_a ^ abs_b, ((~abs_a) & abs_b) << 1
        sum_of_ints = abs_a * sign
        return sum_of_ints
# Runtime: 60 ms, faster than 6.07% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 13.7 MB, less than 74.57% of Python3 online submissions for Sum of Two Integers.

# both pos and neg ints
# does not pass the last check, says Time Limit Exceeded when submitting
# and then Memory Limit Exceeded on Run Code
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a_is_pos = a > 0
        b_is_pos = b > 0
        abs_a = abs(a)
        abs_b = abs(b)
        neg = True
        print(f'a is: {a_is_pos}')
        print(f'b is: {b_is_pos}')
        # both positive
        if a_is_pos and b_is_pos:
            print(f'both positive')
            array = self.same_signs_array(a, b)
            neg = False
            
        # both negativve
        elif a_is_pos is False and b_is_pos is False:
            print(f'both negative')
            array = self.same_signs_array(abs_a, abs_b)
            print(f'array: {array}')
            
        # abs(a) is bigger
        elif abs(a) >= abs(b):
            print(f'a is bigger')
            array = self.diff_signs_array(abs_a, abs_b)
            if a_is_pos:
                neg = False

        # abs(b) is bigger
        elif abs(b) > abs(a):
            print(f'b is bigger')
            array = self.diff_signs_array(abs_b, abs_a)
            if b_is_pos:
                neg = False

        array_sum = len(array)
        if neg:
            array_sum = -array_sum
        return array_sum

    def same_signs_array(self, num1, num2):
        array = []
        for i in range(num1 + num2):
            print(f'appending: {i}')
            array.append(i)
        return array

    def diff_signs_array(self, bigger_num, smaller_num):
        array = []
        for i in range(bigger_num):
            array.append(i)
        for j in range(abs(smaller_num)):
            array.pop()
        return array



# only works if ints both are positive
class Solution:
    def getSum(self, a: int, b: int) -> int:
        array = []
        # both positive
        for i in range(a):
            array.append(i)
        for j in range(b):
            array.append(j)
        # print(f'array: {array}')
        array_sum = len(array)
        return array_sum
