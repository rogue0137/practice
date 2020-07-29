# 1469. Find All The Lonely Nodes
# https://leetcode.com/problems/find-all-the-lonely-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node: TreeNode, node_list, sibling, has_parent) -> List[int]:   
        # does it have children, implying more than one child
        # True if has two
        # False if has one
        has_children = node.right and node.left
        if node.left:
            self.DFS(node.left, node_list, has_children, True)
        if node.right:
            self.DFS(node.right, node_list, has_children, True)
            
        # REQUIREMENTS
        # 1. must NOT be a sibling
        # 2. must have parent
        if not sibling and has_parent:
            node_list.append(node.val)
        
        return node_list

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        node_list = self.DFS(root, [], False, False)
        return node_list


# Runtime: 52 ms, faster than 88.24% of Python3 online submissions for Find All The Lonely Nodes.
# Memory Usage: 14.4 MB, less than 76.47% of Python3 online submissions for Find All The Lonely Nodes.
