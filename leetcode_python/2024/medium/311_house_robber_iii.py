# https://leetcode.com/problems/house-robber-iii/description/

# Rember to use an interative solution!


from typing import Optional

# Definition for a binary tree node provided by leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Solution
#
# Some common patterns for Depth First Search:
# - uses a stack
# - bottom up approach
# - houses_with_computed_max_profitsization commonly used

# DEFINITION: memoization is an optimization technique that speeds up programs by caching the results 
# of expensive function calls and returning the cached result when the same inputs occur again.
# 
class DFSSolution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # This is the houses_with_computed_max_profitsization. You could also just use `houses_with_computed_max_profits` as the variable name, but
        # sometimes being more explicit makes it easier for me
        houses_with_computed_max_profits = {}
        stack = [root]
        
        while stack:
            # Peek at the top node without removing it
            # This is a bottoms up approach
            node = stack[-1]  
            
            if node:
                if node not in houses_with_computed_max_profits:
                    # Check if we can calculate the result for this node by doing the following:
                    # Do we have?
                    #  - Left child:
                    #   - None: no need to wait for it!
                    #   - in houses_with_computed_max_profits: we've already calculated the result so we don't need to wait for it
                    #  - Right child:
                    #   - None: no need to wait for it!
                    #   - in houses_with_computed_max_profits: We've already calculated the result so we don't need to wait for it
                    if (node.left is None or node.left in houses_with_computed_max_profits) and (node.right is None or node.right in houses_with_computed_max_profits):
                        # Calculate profit excluding the current house
                        profit_excluding_curr_house = houses_with_computed_max_profits.get(node.left, 0) + houses_with_computed_max_profits.get(node.right, 0)
                        
                        # Calculate profit including the current house
                        profit_including_curr_house = node.val
                        if node.left:
                            profit_including_curr_house += houses_with_computed_max_profits.get(node.left.left, 0) + houses_with_computed_max_profits.get(node.left.right, 0)
                        if node.right:
                            profit_including_curr_house += houses_with_computed_max_profits.get(node.right.left, 0) + houses_with_computed_max_profits.get(node.right.right, 0)
                        
                        # Store the maximum profit in houses_with_computed_max_profits
                        houses_with_computed_max_profits[node] = max(profit_including_curr_house, profit_excluding_curr_house)
                        
                        # Remove the processed node from the stack
                        stack.pop()
                    else:
                        # We have to still process results (wait), so add children for future processing
                        if node.left and node.left not in houses_with_computed_max_profits:
                            stack.append(node.left)
                        if node.right and node.right not in houses_with_computed_max_profits:
                            stack.append(node.right)
        
        return houses_with_computed_max_profits[root]

# Approaching this problem using BFS is not recommended because you need a bottoms-up approach, AKA, you need
# to know information from the child nodes before you can do anything with the parent nodes. Thus, you'd have
# to traverse the tree multiple times to get all the informatoin you need when doing a BFS version.


# Example 1:
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Tree structure:
#      3
#    /   \
#   2     3
#    \     \
#     3     1

# Initial state:
# houses_with_computed_max_profits = {}
# stack = [3]  # root node

# LOOP 1
   # node = 3 (root)
   # 3 not in houses_with_computed_max_profits
   # Left child (2) not in houses_with_computed_max_profits, right child (3) not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [3, 2, 3]

# LOOP 2
   # node = 3 (right child of root)
   # 3 not in houses_with_computed_max_profits
   # Left child is None, right child (1) not in houses_with_computed_max_profits
   # Add right child to stack
   # stack is now [3, 2, 3, 1]

# LOOP 3
   # node = 1
   # 1 not in houses_with_computed_max_profits
   # No children, can compute result
   # profit_excluding_curr_house = 0
   # profit_including_curr_house = 1
   # houses_with_computed_max_profits[1] = max(1, 0) = 1
   # Pop 1 from stack
   # stack is now [3, 2, 3]

# LOOP 4
   # node = 3 (right child of root)
   # 3 not in houses_with_computed_max_profits
   # Left child is None, right child (1) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(1, 0) = 1
   # profit_including_curr_house = 3 + 0 = 3
   # houses_with_computed_max_profits[3] = max(3, 1) = 3
   # Pop 3 from stack
   # stack is now [3, 2]

# LOOP 5
   # node = 2
   # 2 not in houses_with_computed_max_profits
   # Left child is None, right child (3) not in houses_with_computed_max_profits
   # Add right child to stack
   # stack is now [3, 2, 3]

# LOOP 6
   # node = 3 (right child of 2)
   # 3 not in houses_with_computed_max_profits
   # No children, can compute result
   # profit_excluding_curr_house = 0
   # profit_including_curr_house = 3
   # houses_with_computed_max_profits[3] = max(3, 0) = 3
   # Pop 3 from stack
   # stack is now [3, 2]

# LOOP 7
   # node = 2
   # 2 not in houses_with_computed_max_profits
   # Left child is None, right child (3) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(3, 0) = 3
   # profit_including_curr_house = 2 + 0 = 2
   # houses_with_computed_max_profits[2] = max(2, 3) = 3
   # Pop 2 from stack
   # stack is now [3]

# LOOP 8
   # node = 3 (root)
   # 3 not in houses_with_computed_max_profits
   # Left child (2) in houses_with_computed_max_profits, right child (3) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(2, 0) + houses_with_computed_max_profits.get(3, 0) = 3 + 3 = 6
   
   # Calculate profit including the current house:
   # profit_including_curr_house = node.val (3)
   # For left child (2):
   #   - left.left is null, so add 0
   #   - left.right is 3, so add houses_with_computed_max_profits.get(3, 0) = 3
   # For right child (3):
   #   - right.left is null, so add 0
   #   - right.right is 1, so add houses_with_computed_max_profits.get(1, 0) = 1
   # profit_including_curr_house = 3 + 0 + 3 + 0 + 1 = 7
   
   # houses_with_computed_max_profits[3] = max(7, 6) = 7
   # Pop 3 from stack
   # stack is now empty

# Return houses_with_computed_max_profits[root] = 7


# Example 2:
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Tree structure:
#      3
#    /   \
#   4     5
#  / \     \
# 1   3     1

# Initial state:
# houses_with_computed_max_profits = {}
# stack = [3]  # root node

# LOOP 1
   # node = 3 (root)
   # 3 not in houses_with_computed_max_profits
   # Left child (4) not in houses_with_computed_max_profits, right child (5) not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [3, 4, 5]

# LOOP 2
   # node = 5
   # 5 not in houses_with_computed_max_profits
   # Left child is None, right child (1) not in houses_with_computed_max_profits
   # Add right child to stack
   # stack is now [3, 4, 5, 1]

# LOOP 3
   # node = 1 (right child of 5)
   # 1 not in houses_with_computed_max_profits
   # No children, can compute result
   # profit_excluding_curr_house = 0
   # profit_including_curr_house = 1
   # houses_with_computed_max_profits[1] = max(1, 0) = 1
   # Pop 1 from stack
   # stack is now [3, 4, 5]

# LOOP 4
   # node = 5
   # 5 not in houses_with_computed_max_profits
   # Left child is None, right child (1) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(1, 0) = 1
   # profit_including_curr_house = 5 + 0 = 5
   # houses_with_computed_max_profits[5] = max(5, 1) = 5
   # Pop 5 from stack
   # stack is now [3, 4]

# LOOP 5
   # node = 4
   # 4 not in houses_with_computed_max_profits
   # Left child (1) not in houses_with_computed_max_profits, right child (3) not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [3, 4, 1, 3]

# LOOP 6
   # node = 3 (right child of 4)
   # 3 not in houses_with_computed_max_profits
   # No children, can compute result
   # profit_excluding_curr_house = 0
   # profit_including_curr_house = 3
   # houses_with_computed_max_profits[3] = max(3, 0) = 3
   # Pop 3 from stack
   # stack is now [3, 4, 1]

# LOOP 7
   # node = 1 (left child of 4)
   # 1 not in houses_with_computed_max_profits
   # No children, can compute result
   # profit_excluding_curr_house = 0
   # profit_including_curr_house = 1
   # houses_with_computed_max_profits[1] = max(1, 0) = 1
   # Pop 1 from stack
   # stack is now [3, 4]

# LOOP 8
   # node = 4
   # 4 not in houses_with_computed_max_profits
   # Left child (1) in houses_with_computed_max_profits, right child (3) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(1, 0) + houses_with_computed_max_profits.get(3, 0) = 1 + 3 = 4
   # profit_including_curr_house = 4 + 0 + 0 = 4
   # houses_with_computed_max_profits[4] = max(4, 4) = 4
   # Pop 4 from stack
   # stack is now [3]

# LOOP 9
   # node = 3 (root)
   # 3 not in houses_with_computed_max_profits
   # Left child (4) in houses_with_computed_max_profits, right child (5) in houses_with_computed_max_profits
   # Can compute result
   # profit_excluding_curr_house = houses_with_computed_max_profits.get(4, 0) + houses_with_computed_max_profits.get(5, 0) = 4 + 5 = 9
   
   # Calculate profit including the current house:
   # profit_including_curr_house = node.val (3)
   # For left child (4):
   #   - left.left is 1, so add houses_with_computed_max_profits.get(1, 0) = 1
   #   - left.right is 3, so add houses_with_computed_max_profits.get(3, 0) = 3
   # For right child (5):
   #   - right.left is null, so add 0
   #   - right.right is 1, so add houses_with_computed_max_profits.get(1, 0) = 1
   # profit_including_curr_house = 3 + 1 + 3 + 0 + 1 = 8
   
   # houses_with_computed_max_profits[3] = max(9, 8) = 9
   # Pop 3 from stack
   # stack is now empty

# Return houses_with_computed_max_profits[root] = 9

