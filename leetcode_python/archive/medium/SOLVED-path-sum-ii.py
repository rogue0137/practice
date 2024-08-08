# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # root-to-leaf paths = DFS
    def DFS(
            self, 
            node: TreeNode,
            leftover_sum: int,
            list_of_nodes: List[int],
            list_Of_paths: List[List[int]]):

        if not node:
            return 

        # Add the current node to the running list of nodes
        list_of_nodes.append(node.val)
        
        # REQUIREMENTS:
        # 1) LEAF NODE = has no children (no left or right) 
        # 2) Leftover sum equals that node's value
        if leftover_sum == node.val and not node.left and not node.right:
            list_Of_paths.append(list(list_of_nodes))
        else:    
            # At least one requirement not met
            # If sum is the requirment not met, it's all good because we'll hit
            # the `if not node line`
            # If we still have nodes, awesome! Let's keep going
            self.DFS(node.left, leftover_sum - node.val, list_of_nodes, list_Of_paths)
            self.DFS(node.right, leftover_sum - node.val, list_of_nodes, list_Of_paths)
            
        # pop node once you've checked all it's children
        list_of_nodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        list_Of_paths = []
        self.DFS(root, sum, [], list_Of_paths)
        return list_Of_paths

# Runtime: 48 ms, faster than 73.26% of Python3 online submissions for Path Sum II.
# Memory Usage: 15 MB, less than 81.87% of Python3 online submissions for Path Sum II.
