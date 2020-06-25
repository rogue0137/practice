# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, node: TreeNode) -> List[int]:
        tree_order = []
        if node and node.left:
            tree_order.extend(self.inorderTraversal(node.left))
        if node:
            tree_order.append(node.val)
        if node and node.right:
            tree_order.extend(self.inorderTraversal(node.right))
        return tree_order

# Runtime: 48 ms, faster than 8.94% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.8 MB, less than 74.18% of Python3 online submissions for Binary Tree Inorder Traversal.