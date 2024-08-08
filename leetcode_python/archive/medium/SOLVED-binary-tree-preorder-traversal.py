# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, node: TreeNode) -> List[int]:
        tree_order = []
        if node is None:
            return []
        tree_order.append(node.val)
        if node and node.left: 
            tree_order.extend(self.preorderTraversal(node.left))
        if node and node.right:
            tree_order.extend(self.preorderTraversal(node.right))
        return tree_order

# Runtime: 28 ms, faster than 75.14% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.9 MB, less than 27.52% of Python3 online submissions for Binary Tree Preorder Traversal.