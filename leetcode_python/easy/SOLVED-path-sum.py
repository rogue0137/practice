# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
class Solution:
    def hasPathSum(self, node: TreeNode, sum: int) -> bool:
        if not node:
            return False

        sum = sum - node.val
        if not node.left and not node.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(node.left, sum) or self.hasPathSum(node.right, sum)
# Runtime: 56 ms, faster than 18.01% of Python3 online submissions for Path Sum.
# Memory Usage: 15.6 MB, less than 66.91% of Python3 online submissions for Path Sum.

# node, curr_sum = de.pop()
# if node.right: de.append(node.right, curr_sum - node.right.val)
# if node.left: de.append(node.left, curr_sum - node.left.val)
# <--- this is DFS (preorder: node, left, right)
class Solution:
    def hasPathSum(self, node: TreeNode, sum: int) -> bool:
    if not node:
            return False

        de = [(node, sum - node.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  

# node, curr_sum = de.pop(0)
# if node.left: de.append(node.left, curr_sum - node.left.val)
# if node.right: de.append(node.right, curr_sum - node.right.val)
# <--- this is BFS
class Solution:
    from collections import dequeue 
    def hasPathSum(self, node: TreeNode, sum: int) -> bool:
        if node.left:
            de.append(node.left, sum)

