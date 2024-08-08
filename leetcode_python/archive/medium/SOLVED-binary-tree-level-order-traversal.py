# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# with helper
class Solution:
    def levelOrder(self, node: TreeNode) -> List[List[int]]:
    tree_order = []
    level = 0
    self.dfs(node, level, tree_order)
    return tree_order
    # depth first search
    def dfs(self, node, level, tree_order):
        if not node:
            return 
        # if level not already on array, this creates it
        if len(tree_order) < level+1:
            tree_order.append([])
        # add value to appropriate level
        tree_order[level].append(node.val)
        # if children, keep going
        self.dfs(node.left, level+1, tree_order)
        self.dfs(node.right, level+1, tree_order)

# Runtime: 32 ms, faster than 82.08% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.3 MB, less than 21.41% of Python3 online submissions for Binary Tree Level Order Traversal.


# with helper, but checking for children not node
class Solution:
    def levelOrder(self, node: TreeNode) -> List[List[int]]:
        tree_order = []
        level = 0
        if node:
            self.dfs(node, level, tree_order)
        return tree_order
    # depth first search
    def dfs(self, node, level, tree_order):
        # if level not already on array, this creates it
        if len(tree_order) < level+1:
            tree_order.append([])
        # add value to appropriate level
        tree_order[level].append(node.val)
        # if children, keep going
        if node.left:
            self.dfs(node.left, level+1, tree_order)
        if node.right:
            self.dfs(node.right, level+1, tree_order)
# Checking for node w/in dfs much faster because it means that you don't
# need the "if node " in levelOrder and then "if left/if right" in dfs:
# Runtime: 60 ms, faster than 7.63% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.3 MB, less than 21.41% of Python3 online submissions for Binary Tree Level Order Traversal.

# using a queue
from collections import deque

class Solution:
    def levelOrder(self, node: TreeNode) -> List[List[int]]:
        tree_order = []
        # you basically need a queue so you can pop left
        # any array would only let you pop right
        queue = deque([(node, 0)])
        while queue and node:
            node, level = queue.popleft()
            if len(tree_order) < level+1:
                tree_order.append([])
            tree_order[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return tree_order
# Runtime: 28 ms, faster than 94.30% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.2 MB, less than 31.09% of Python3 online submissions for Binary Tree Level Order Traversal.