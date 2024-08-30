# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        nodes = [ root ]

        while len(nodes):
            node = nodes.pop()

            if node.val >= low and node.val <= high:
                range_sum += node.val
            
            if node.left:
                nodes.append(node.left)
            
            if node.right:
                nodes.append(node.right)
        
        return range_sum
