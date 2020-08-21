# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE SOLUTION
from typing import List


class Solution:
    def DFS(self, node: TreeNode, level: int, list_of_leaves: List[int]):
        children = node.right or node.left
        if node.left:
            self.DFS(node.left, level + 1, list_of_leaves)
            
        if node.right:
            self.DFS(node.right, level + 1, list_of_leaves)

        # REQUIREMENTS
        # 1. has no children
        if not children:
            list_of_leaves.append(level)
        return list_of_leaves
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        list_of_leaves = self.DFS(root, 1, [])
        list_of_leaves.sort()
        return list_of_leaves[0]


# Runtime: 44 ms, faster than 80.27% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 15.9 MB, less than 10.62% of Python3 online submissions for Minimum Depth of Binary Tree.


# ITERATIVE SOLUTION
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0        
        
        node = root
        depth = 1 # we're at first level
        first_stack_input = (node, depth)
        stack = [first_stack_input]
        minDepth = float("inf") # infitely large number
        
        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                minDepth = min(depth, minDepth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return minDepth 

# Runtime: 80 ms, faster than 11.15% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 15 MB, less than 78.68% of Python3 online submissions for Minimum Depth of Binary Tree.