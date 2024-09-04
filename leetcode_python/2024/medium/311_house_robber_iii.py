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
# - memoization commonly used
class DFSSolution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        memo = {}
        stack = [root]
        
        while stack:
            # Peek at the top node without removing it
            # This is a bottoms up approach
            node = stack[-1]  
            
            if node:
                if node not in memo:
                    # Check if we can calculate the result for this node by doing the following:
                    # Do we have?
                    #  - Left child:
                    #   - None: no need to wait for it!
                    #   - in Memo: we've already calculated the result so we don't need to wait for it
                    #  - Right child:
                    #   - None: no need to wait for it!
                    #   - in Memo: We've already calculated the result so we don't need to wait for it
                    if (node.left is None or node.left in memo) and (node.right is None or node.right in memo):
                        # Calculate profit excluding the current house
                        profit_excluding_curr_house = memo.get(node.left, 0) + memo.get(node.right, 0)
                        
                        # Calculate profit including the current house
                        profit_including_curr_house = node.val
                        if node.left:
                            profit_including_curr_house += memo.get(node.left.left, 0) + memo.get(node.left.right, 0)
                        if node.right:
                            profit_including_curr_house += memo.get(node.right.left, 0) + memo.get(node.right.right, 0)
                        
                        # Store the maximum profit in memo
                        memo[node] = max(profit_including_curr_house, profit_excluding_curr_house)
                        
                        # Remove the processed node from the stack
                        stack.pop()
                    else:
                        # We have to still process results (wait), so add children for future processing
                        if node.left and node.left not in memo:
                            stack.append(node.left)
                        if node.right and node.right not in memo:
                            stack.append(node.right)
        
        return memo[root]

# Approaching this problem using BFS is not recommended because you need a bottoms-up approach, AKA, you need
# to know information from the child nodes before you can do anything with the parent nodes. Thus, you'd have
# to traverse the tree multiple times to get all the informatoin you need.
