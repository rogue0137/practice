# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# DRAWING: https://docs.google.com/drawings/d/1cm23KVkc2n8CN6rfxlBAhhP9-wWvtWOeOEg4LYKgKKU/edit



# IF YOU'RE COMING FROM WWC: THIS IS THE CODE I WROTE FROM OUR SESSION
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # max_sum_of_all_branches is our max_sum from the diagram
        # if it does not make sense why we are returning this, please spend time reading
        #   the section in DFS where it gets set
        max_lateral_branch, max_sum = self.DFS(root)
        
        return max_sum
    
    def DFS(self, node):
        # Go all the way down (Depth First Search)
        # POSTORDER: left -> right -> root
        
        # always need a scenario for when node does not exist
        if not node:
            # (max_lateral_branch, max_branches_including_triangles)
            # Both of these should not be set to 0 because there are actual negative values int he trees
            #   float("-inf") is equal to setting an increadibly large, 
            #   almost infinite negative value
            return (float("-inf"), float("-inf"))
        
        # start left (postorder)
        # LTB: LEFT LATERAL BRANCH from max_lateral_branch
        # LMIT: LEFT MAX INCLUDING LATERAL AND TRIANGLE BRANCHES from max_branches_including_triangles
        LLB, LMIT = self.DFS(node.left)
        
        # then go right (postorder)
        # RSB: RIGHT LATERAL BRANCH from max_lateral_branch
        # RMIT: RIGHT MAX INCLUDING LATERAL AND TRIANGLE BRANCHES from max_branches_including_triangles
        RLB, RMIT = self.DFS(node.right)
        
        
        # IS LEFT OR RIGHT LATERAL BRANCH BIGGER?
        max_child_lateral_branch = max(LLB, RLB)    
        
        # HAVE NOT YET EVALUATED THE NODE AT THIS LEVEL
        # node itself is finally evaluated (postorder)
        max_lateral_branch = max(max_child_lateral_branch + node.val, node.val)
        
        # ARE LATERAL BRANCHES OR TRIANGLES BIGGER?
        # CREATE A TRIANGLE: LLB, RSB, node.val
        curr_triangle = LLB + RLB + node.val
        max_branch = max(max_lateral_branch, curr_triangle)

        # MAX SUM in our diagram
        # LMIT: is the node.left child's lateral and triangle biggest?
        # RMIT: is the node.right child's lateral and triangle biggest?
        # max_sum_of_all_branches: is the max_branch of this one node biggest? 
        max_sum_of_all_branches = max(LMIT, RMIT, max_branch)
        
        return max_lateral_branch, max_sum_of_all_branches



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
