# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/


# ITERATIVE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TREE/GRAPH LOOKS LIKE THIS

# L1:                    1
#                         \
# L2:                     2
#                        / 
# L3:                   3

class Solution:
    def postorderTraversal(self, node: TreeNode) -> List[int]:
        stack, postorder_array = [], []

        while node or stack: # node exists(1)
            # set up the stack
            while node: # node exists(1)
                if node.right: # 2
                    stack.append(node.right) # stack: [2]
                stack.append(node) # stack: [2, 1]
                node = node.left # None
            node = stack.pop()
            # if stack and not leftmost
            if stack and node.right == stack[-1]:
                # swap them and try again
                stack[-1] = node
                node = node.right
            else:
                postorder_array.append(node.val)
                node = None
        return postorder_array

# NOTE: for stack I am writing the value of the node
# not node itself, even though we are actually adding the node object
# ROUND 1
    # node exists -> 1
        # node exists -> 1
        # node.right exists -> 2
            # append node.right to stack -> [2]
        # append node to stack -> [2, 1]
    # no more node so we exist `while node` loop
    # pop node from stack -> 1
    # stack still exists [2] AND node.right (1) is equal to stack[-1] (1)
        # we must switch the order
            # stack is now [1]
            # node is now [2]
# ROUND 2
    # node exists -> 2
    # node.right doesnt exist so skip
    # append node to stack [1, 2]
    # node becomes node.left
# ROUND 3
    # node exists so stay in `while node` loop -> 3
    # node.right doesn't exist so skip
    # append node to stack [1, 2, 3]
    # pop node from stack -> [3]
    # stack still exists [1, 2], BUT node.right (None) is not equal to stack[-1] (2)
        # add value of node to postorder_array -> [3]
        # set node to None
# ROUND 4
    # pop node from stack -> 2
    # stack still exists [1], node.right (None) is not equal to stack [-1] (1)
        # add value of node to postorder_array -> [3, 2]
        # set node to None
# ROUND 5
    # pop node from stack --> 1
    # stack no longer exists
        # add value of node to postoerder_array --> [3, 2, 1]
        # set node to None
    # exist `while node or stack` because neither exists now





# Runtime: 36 ms, faster than 39.77% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 14 MB, less than 14.74% of Python3 online submissions for Binary Tree Postorder Traversal.

# RECURSIVE
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