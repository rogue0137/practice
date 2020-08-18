# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
