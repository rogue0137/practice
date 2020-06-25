# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, node: TreeNode) -> List[int]:
        tree_order = []
        if node and node.left:
            tree_order.extend(self.postorderTraversal(node.left))
        if node and node.right:
            tree_order.extend(self.postorderTraversal(node.right))
        if node:
            tree_order.append(node.val)
        return tree_order

# Runtime: 44 ms, faster than 10.38% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.9 MB, less than 22.21% of Python3 online submissions for Binary Tree Postorder Traversal.