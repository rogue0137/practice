# 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node): # 
        # depth: checking for children and going down the tree
        if node.left:
            left_node, left_children = self.DFS(node.left)
        else:
            left_node, left_children = (0, 0)
        if node.right:
            right_node, right_children = self.DFS(node.right)
        else:
            right_node, right_children = (0, 0)

        only_node = node.val + left_children + right_children 
        children = max(left_node + right_node,
                       left_node + right_children,
                       left_children + right_children,
                       left_children + right_node)

        return only_node, children

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.DFS(root))
# Runtime: 48 ms, faster than 89.47% of Python3 online submissions for House Robber III.
# Memory Usage: 15.9 MB, less than 69.74% of Python3 online submissions for House Robber III.

