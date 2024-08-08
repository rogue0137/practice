# 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, list_of_nodes):
        if node.left:
            self.DFS(node.left, list_of_nodes)
        if node.right:
            self.DFS(node.right, list_of_nodes)
        # REQUIREMENTS
        # 1.  has no children
        has_no_children = not node.left and not node.right
        if has_no_children:
            list_of_nodes.append(node.val)
        return list_of_nodes
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1 = []
        list2 = []
        
        self.DFS(root1, list1)
        self.DFS(root2, list2)
        
        if list1 == list2:
            return True
        else:
            return False

# Runtime: 52 ms, faster than 16.67% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 14 MB, less than 40.74% of Python3 online submissions for Leaf-Similar Trees.