# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Rember to use an interative solution!

from typing import Optional

# Definition for a binary tree node provided by leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        max_sum = float('-inf')

        # In order to solve this problem, we need to make multiple "visits" to nodes:
        # - 0: First visit, need to process left child
        # - 1: Second visit, need to process right child
        # - 2: Third visit, need to compute the max path sum for this node

        # We're at the root here and have not processed it yet, so our visit_count should be 0
        stack = [(root, 0)]
        
        while stack:
            node, visit_count = stack.pop()
            
            if node:
                if visit_count == 0:
                    stack.append((node, 1))
                    stack.append((node.left, 0))
                elif visit_count == 1:
                    stack.append((node, 2))
                    stack.append((node.right, 0))
                else:
                    left_sum = node.left.val if node.left else 0
                    right_sum = node.right.val if node.right else 0
                    
                    # IMPORTANT STEP 1: Get current max sum by looking at
                    # - Just the node itself (if both left_sum and right_sum are negative or zero)
                    # - The node and its left subtree (if right_sum is negative or zero)
                    # - The node and its right subtree (if left_sum is negative or zero)
                    # - The node and both subtrees (if everything is positive)

                    # Why are we using max(0, side_sum)?
                    #   If left_sum or right_sum is negative, including it would decrease our path sum.
                    #   By using max(0, side_sum), we choose to either:
                    #   1. Include the side if it's positive (increases our sum)
                    #   2. Exclude the side if it's negative (by choosing 0 instead)
                    # This allows us to consider all possible combinations: node alone, node with left, node with right, or node with both.
                    max_sum = max(max_sum, node.val + max(0, left_sum) + max(0, right_sum))
                    
                    # IMPORTANT STEP 2: Prepare this node for use in higher-level calculations
                    # We update node.val to represent the best path that:
                    #   1. Starts at this node
                    #   2. Goes downwards through at most one child (left OR right)
                    # Why? This value will be used when we calculate paths for this node's parent
                    node.val += max(0, max(left_sum, right_sum))

        
        return max_sum

# Example:
# Input: root = [10,5,15,3,7,12,18,1,4,6,null,null,null,16,20]
# Output: 81

# Tree looks like
#         10
#       /    \
#      5      15
#    /   \   /  \
#   3     7 12   18
#  / \   /       / \
# 1   4 6       16  20

# Max sum path
#          *10*
#        /      \
#      *5*       *15*
#    /     \    /    \
#   3      *7* 12    *18*
#  / \     /         /  \
# 1   4   6        16  *20*

# Maximum Path Sum: 7 + 5 + 10 + 15 + 18 + 20 = 81

# Initial state:
# max_sum = float('-inf')
# stack = [(10, 0)]  # (node, visit_count)

# LOOP 1
   # Pop (10, 0) from stack
   # 10 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 0), (15, 0)]

# LOOP 2
   # Pop (15, 0) from stack
   # 15 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 0), (15, 1), (12, 0), (18, 0)]

# LOOP 3
   # Pop (18, 0) from stack
   # 18 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 0), (15, 1), (12, 0), (18, 1), (16, 0), (20, 0)]

# LOOP 4 (Process leaf node 20)
   # Pop (20, 0) from stack
   # max_sum = max(-inf, 20) = 20
   # node.val update: 20 += max(0, max(0, 0)) = 20 (no change)
   # stack is now [(10, 1), (5, 0), (15, 1), (12, 0), (18, 1), (16, 0)]

# LOOP 5 (Process leaf node 16)
   # Pop (16, 0) from stack
   # max_sum = max(20, 16) = 20
   # node.val update: 16 += max(0, max(0, 0)) = 16 (no change)
   # stack is now [(10, 1), (5, 0), (15, 1), (12, 0), (18, 1)]

# LOOP 6
   # Pop (18, 1) from stack
   # Process node 18:
   #   left_sum = 16, right_sum = 20
   #   max_sum = max(20, 18 + 16 + 20) = 54
   #   node.val update: 18 += max(0, max(16, 20)) = 38
   # stack is now [(10, 1), (5, 0), (15, 1), (12, 0)]

# LOOP 7 (Process leaf node 12)
   # Pop (12, 0) from stack
   # max_sum = max(54, 12) = 54
   # node.val update: 12 += max(0, max(0, 0)) = 12 (no change)
   # stack is now [(10, 1), (5, 0), (15, 1)]

# LOOP 8
   # Pop (15, 1) from stack
   # Process node 15:
   #   left_sum = 12, right_sum = 38
   #   max_sum = max(54, 15 + 12 + 38) = 65
   #   node.val update: 15 += max(0, max(12, 38)) = 53
   # stack is now [(10, 1), (5, 0)]

# LOOP 9
   # Pop (5, 0) from stack
   # 5 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 1), (3, 0), (7, 0)]

# LOOP 10
   # Pop (7, 0) from stack
   # 7 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 1), (3, 0), (7, 1), (6, 0)]

# LOOP 11 (Process leaf node 6)
   # Pop (6, 0) from stack
   # max_sum = max(65, 6) = 65
   # node.val update: 6 += max(0, max(0, 0)) = 6 (no change)
   # stack is now [(10, 1), (5, 1), (3, 0), (7, 1)]

# LOOP 12
   # Pop (7, 1) from stack
   # Process node 7:
   #   left_sum = 6, right_sum = 0
   #   max_sum = max(65, 7 + 6 + 0) = 65
   #   node.val update: 7 += max(0, max(6, 0)) = 13
   # stack is now [(10, 1), (5, 1), (3, 0)]

# LOOP 13
   # Pop (3, 0) from stack
   # 3 not in houses_with_computed_max_profits
   # Add children to stack
   # stack is now [(10, 1), (5, 1), (3, 1), (1, 0), (4, 0)]

# LOOP 14 (Process leaf node 4)
   # Pop (4, 0) from stack
   # max_sum = max(65, 4) = 65
   # node.val update: 4 += max(0, max(0, 0)) = 4 (no change)
   # stack is now [(10, 1), (5, 1), (3, 1), (1, 0)]

# LOOP 15 (Process leaf node 1)
   # Pop (1, 0) from stack
   # max_sum = max(65, 1) = 65
   # node.val update: 1 += max(0, max(0, 0)) = 1 (no change)
   # stack is now [(10, 1), (5, 1), (3, 1)]

# LOOP 16
   # Pop (3, 1) from stack
   # Process node 3:
   #   left_sum = 1, right_sum = 4
   #   max_sum = max(65, 3 + 1 + 4) = 65
   #   node.val update: 3 += max(0, max(1, 4)) = 7
   # stack is now [(10, 1), (5, 1)]

# LOOP 17
   # Pop (5, 1) from stack
   # Process node 5:
   #   left_sum = 7, right_sum = 13
   #   max_sum = max(65, 5 + 7 + 13) = 65
   #   node.val update: 5 += max(0, max(7, 13)) = 18
   # stack is now [(10, 1)]

# LOOP 18
   # Pop (10, 1) from stack
   # Process root node 10:
   #   left_sum = 18, right_sum = 53
   #   max_sum = max(65, 10 + 18 + 53) = 81
   #   node.val update: 10 += max(0, max(18, 53)) = 63
   # stack is now empty

# Return max_sum = 81
