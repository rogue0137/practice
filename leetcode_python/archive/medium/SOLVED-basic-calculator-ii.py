# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# Use a stack

class Solution:
    def calculate(self, s: str) -> int:
        len_s = len(s)
        numbers_stack = []
        num = 0
        # start with plus because you're going to append the first num you see
        sign = '+' 
        for i in range(len_s):
            print(f'i: {i}, stack: {numbers_stack}')
            char = s[i]
            print(f'char: {char}')
            if char.isdigit():
                # move num over to the left to add a new ones place
                num = (num * 10) + int(char)
            # need to append last num using last sign if last loop
            if char in '*/+-' or i == len_s - 1:
                # using previous sign since you have not yet updated sign to char
                if sign == '+':
                    numbers_stack.append(num)
                if sign == '-':
                    numbers_stack.append(-num)
                if sign == '*':
                    new_num = numbers_stack.pop() * num
                    numbers_stack.append(new_num)
                if sign == '/':
                    new_num = int(numbers_stack.pop() / num)
                    numbers_stack.append(new_num)
                # reset/update values
                num = 0
                sign = char
        sum_of_stack = sum(numbers_stack)
        return sum_of_stack

# Runtime: 84 ms, faster than 85.86% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.6 MB, less than 52.67% of Python3 online submissions for Basic Calculator II.