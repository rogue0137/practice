# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# DRAWING: https://docs.google.com/drawings/d/1cm23KVkc2n8CN6rfxlBAhhP9-wWvtWOeOEg4LYKgKKU/edit

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _, running_max_path_sum = self.dfs(root)
        return running_max_path_sum

    # DFS because you're going by path
    # postorder because L, R, then root
    def dfs(self, node: TreeNode):
        # IF NO NODE:
        # max_single_branch will be 0 becase there are no branches 
        # max_running_path_sum will be set to float("-inf")
        #   float("-inf") is equal to setting an increadibly large, 
        #   almost infinite negative value
        if not node:
            return (0, float("-inf"))

        # LEFT AND RIGHT SIDES ON THEIR OWN
        # LSB: left_single_branch
        # LS: running_max_sum_for_left_side
        LSB, LS = self.dfs(node.left)
        # RSB: right_single_branch
        # RS: running_max_sum_for_right_side
        RSB, RS = self.dfs(node.right)

        # IS L OR R BIGGER
        max_child_single_branch = max(LSB, RSB)

        # WHAT IF WE ADD THE NODE'S VALUE
        # is the branch with node or the node by itself biggger?
        max_single_branch = max(max_child_single_branch + node.val,
                                node.val)

        # we can either have a single lateral branch as the highest sum
        # or a triangle branch
        # CHECK THE TRIANGLE BRANCH
        max_single_triangle = max(
            max_single_branch, 
            LSB + node.val + RSB)

        # GET THE RUNNING SUM 
        # FROM L AND R AND TRIANGLE
        running_max_path_sum = max(
            LS,
            RS,
            max_single_triangle)
        
        return (max_single_branch, running_max_path_sum)

# Runtime: 96 ms, faster than 71.30% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 20.5 MB, less than 73.84% of Python3 online submissions for Binary Tree Maximum Path Sum.