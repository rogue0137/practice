# 1167. Minimum Cost to Connect Sticks
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        sticks.sort()
        cost = 0
        stack = []

        while len(sticks) + len(stack) > 1:
            print('LOOP')
            print(f'len sticks: {len(sticks)}')
            print(f'len stacks: {len(stack)}')
            print('a')
            a = self.leftpop(sticks, stack)
            print('b')
            b = self.leftpop(sticks, stack)
            print(f'a: {a}, b: {b}')
            curr_cost = a+b
            print(f'cost before addition: {cost}')
            cost += curr_cost
            print(f'new cost: {cost}')
            print(f'appending to stack')
            stack.append(curr_cost)
            print(f'stack: {stack}')

        return cost

    def leftpop(self, sticks: List[int], stack: List[int]) -> int:
        if not sticks:
            print(f'no sticks, popping first from stack')
            return stack.pop(0)
        if not stack:
            print(f'no stack, popping first from sticks')
            return sticks.pop(0)
        if sticks[0] < stack[0]:
            print(f'sticks bigger than stack')
            return sticks.pop(0)
        else:
            print(f'stack bigger than or equal to sticks')
            return stack.pop(0)

# Without comments
# Runtime: 436 ms, faster than 23.45% of Python3 online submissions for Minimum Cost to Connect Sticks.
# Memory Usage: 14.6 MB, less than 65.28% of Python3 online submissions for Minimum Cost to Connect Sticks.

# RETRY USING HEAP