104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

# this is taking the solutoin for binary-tree-level-order-traversal
# and adding something to check the len instead of the returned tree
class Solution:
    def maxDepth(self, node: TreeNode) -> int:
        tree_order = []
        level = 0
        self.dfs(node, level, tree_order)
        tree_depth = len(tree_order)
        return tree_depth
    # depth first search
    def dfs(self, node, level, tree_order):
        if not node:
            return
        # if level not already on array, this creates it
        new_level = level + 1
        if len(tree_order) < new_level:
            tree_order.append([])
        # add value to appropriate level
        tree_order[level].append(node.val)
        # if children, keep going
        if node.left:
            self.dfs(node.left, level+1, tree_order)
        if node.right:
            self.dfs(node.right, level+1, tree_order)

# Runtime: 44 ms, faster than 53.33% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.8 MB, less than 15.73% of Python3 online submissions for Maximum Depth of Binary Tree.

# using simple recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def maxDepth(self, node: TreeNode) -> int:
        # if not node seems to be a pattern in trees
        if not node: 
            return 0 
        else: 
            left_height = self.maxDepth(node.left) 
            right_height = self.maxDepth(node.right)
            # print(f'node: {node}')
            # print(f'max + 1: {max(left_height, right_height)} + 1')
            # this plus one here enables the height to increase per level
            # we go down
            return max(left_height, right_height) + 1 
# Not faster, but easier to read! 
# Runtime: 52 ms, faster than 17.59% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.5 MB, less than 29.38% of Python3 online submissions for Maximum Depth of Binary Tree.
        