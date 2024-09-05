# https://leetcode.com/problems/same-tree/description/

# These solutions are specifically only showing NON-recursive approaches.
# In my experience, interviewers generally prefer iterative (stacks and queues) over recursive solutoins. 


from typing import Optional

# Definition for a binary tree node provided by leetcode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS Solution -- using a queue, processing level by level
class BFSSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # First, handle the base cases:
        # If both trees are empty (None), they are the same
        if p is None and q is None:
            return True
        
        # If one tree is empty and the other is not, they are different
        if p is None or q is None:
            return False
        
        # Initialize a queue with the root nodes of both trees
        queue = [(p, q)]
        
        # Continue processing until we've checked all nodes
        while queue:
            # Dequeue the next pair of nodes
            # remember: .pop(0) pops from the front
            node_p, node_q = queue.pop(0)
            
            # Compare the values of the current nodes
            if node_p.val != node_q.val:
                return False
            
            # Check left children
            if node_p.left and node_q.left:
                # Both trees have left children, enqueue them for comparison
                queue.append((node_p.left, node_q.left))
            elif node_p.left or node_q.left:
                # Only one tree has a left child, so the trees are different
                return False
            
            # Check right children
            if node_p.right and node_q.right:
                # Both trees have right children, enqueue them for comparison
                queue.append((node_p.right, node_q.right))
            elif node_p.right or node_q.right:
                # Only one tree has a right child, so the trees are different
                return False
        
        # If we've processed all nodes without finding differences, the trees are the same
        return True

# DFS Solution -- using a stack
class DFSSolution:
    from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Helper function
        def dfs_iterative(node_p, node_q):
            stack = [(node_p, node_q)]
            
            while stack:
                node_p, node_q = stack.pop()
                
                # Base cases
                if node_p is None and node_q is None:
                    continue
                if node_p is None or node_q is None:
                    return False
                
                # Compare values
                if node_p.val != node_q.val:
                    return False
                
                # Because we're simulating DFS, we want make sure we're processing the left subtree before
                # looking at the right subtree.
                # In order to accomplish this with a stack, we need to push right first, left next.  
                # This will ensure the left child is popped off the stack first. 
                stack.append((node_p.right, node_q.right))
                stack.append((node_p.left, node_q.left))
            
            return True
        
        # Start the DFS from the root nodes
        return dfs_iterative(p, q)


# DFS examples

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Initial state:
# stack = [(p, q)] = [(1,1)]

# LOOP 1
   # Pop (1,1) from stack
   # p_node.val = 1, q_node.val = 1
   # 1 == 1 : True
   # right children: stack.append((p.right, q.right)) => (3, 3) => stack is now [(3, 3)]
   # left children: stack.append((p.left, q.left)) => (2, 2) => stack is now [(3, 3), (2, 2)]

# LOOP 2
   # Pop (2,2) from stack
   # p_node.val = 2, q_node.val = 2
   # 2 == 2 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(3, 3), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(3, 3), (None, None), (None, None)]

# LOOP 3
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(3, 3), (None, None)]

# LOOP 4
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(3, 3)]

# LOOP 5
   # Pop (3,3) from stack
   # p_node.val = 3, q_node.val = 3
   # 3 == 3 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(None, None), (None, None)]

# LOOP 6
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(None, None)]

# LOOP 7
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now empty

# Stack is empty, all nodes compared successfully
# Return True


# Example 2
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Initial state:
# stack = [(p, q)] = [(1,1)]

# LOOP 1
   # Pop (1,1) from stack
   # p_node.val = 1, q_node.val = 1
   # 1 == 1 : True
   # right children: stack.append((p.right, q.right)) => (None, 2) => stack is now [(None, 2)]
   # left children: stack.append((p.left, q.left)) => (2, None) => stack is now [(None, 2), (2, None)]

# LOOP 2
   # Pop (2, None) from stack
   # p_node is not None, but q_node is None
   # This is a mismatch, so we return False

# Function returns False, indicating the trees are not the same


# Example 3: Longer True Example
# Both trees look like this
#      5
#    /   \
#   3     8
#  / \   / \
# 1   4 6   9

# Input: p = [5,3,8,1,4,6,9], q = [5,3,8,1,4,6,9]
# Output: true

# Initial state:
# stack = [(p, q)] = [(5,5)]

# LOOP 1
   # Pop (5,5) from stack
   # p_node.val = 5, q_node.val = 5
   # 5 == 5 : True
   # right children: stack.append((p.right, q.right)) => (8, 8) => stack is now [(8, 8)]
   # left children: stack.append((p.left, q.left)) => (3, 3) => stack is now [(8, 8), (3, 3)]

# LOOP 2
   # Pop (3,3) from stack
   # p_node.val = 3, q_node.val = 3
   # 3 == 3 : True
   # right children: stack.append((p.right, q.right)) => (4, 4) => stack is now [(8, 8), (4, 4)]
   # left children: stack.append((p.left, q.left)) => (1, 1) => stack is now [(8, 8), (4, 4), (1, 1)]

# LOOP 3
   # Pop (1,1) from stack
   # p_node.val = 1, q_node.val = 1
   # 1 == 1 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(8, 8), (4, 4), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(8, 8), (4, 4), (None, None), (None, None)]

# LOOP 4
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (4, 4), (None, None)]

# LOOP 5
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (4, 4)]

# LOOP 6
   # Pop (4,4) from stack
   # p_node.val = 4, q_node.val = 4
   # 4 == 4 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(8, 8), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(8, 8), (None, None), (None, None)]

# LOOP 7
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (None, None)]

# LOOP 8
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8)]

# LOOP 9
   # Pop (8,8) from stack
   # p_node.val = 8, q_node.val = 8
   # 8 == 8 : True
   # right children: stack.append((p.right, q.right)) => (9, 9) => stack is now [(9, 9)]
   # left children: stack.append((p.left, q.left)) => (6, 6) => stack is now [(9, 9), (6, 6)]

# LOOP 10
   # Pop (6,6) from stack
   # p_node.val = 6, q_node.val = 6
   # 6 == 6 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(9, 9), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(9, 9), (None, None), (None, None)]

# LOOP 11
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(9, 9), (None, None)]

# LOOP 12
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(9, 9)]

# LOOP 13
   # Pop (9,9) from stack
   # p_node.val = 9, q_node.val = 9
   # 9 == 9 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(None, None), (None, None)]

# LOOP 14
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(None, None)]

# LOOP 15
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now empty

# Stack is empty, all nodes compared successfully
# Return True


# Example 4: Longer False Example
# Trees look like
# Tree One:
#     5
#    /   \
#   3     8
#  / \   / \
# 1   4 6   9
# Tree Two:
#      5
#    /   \
#   3     8
#  / \   / \
# 1   4 7   9

# Input: 
# p = [5,3,8,1,4,6,9]
# q = [5,3,8,1,4,7,9]
# Output: false

# Initial state:
# stack = [(p, q)] = [(5,5)]

# LOOP 1
   # Pop (5,5) from stack
   # p_node.val = 5, q_node.val = 5
   # 5 == 5 : True
   # right children: stack.append((p.right, q.right)) => (8, 8) => stack is now [(8, 8)]
   # left children: stack.append((p.left, q.left)) => (3, 3) => stack is now [(8, 8), (3, 3)]

# LOOP 2
   # Pop (3,3) from stack
   # p_node.val = 3, q_node.val = 3
   # 3 == 3 : True
   # right children: stack.append((p.right, q.right)) => (4, 4) => stack is now [(8, 8), (4, 4)]
   # left children: stack.append((p.left, q.left)) => (1, 1) => stack is now [(8, 8), (4, 4), (1, 1)]

# LOOP 3
   # Pop (1,1) from stack
   # p_node.val = 1, q_node.val = 1
   # 1 == 1 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(8, 8), (4, 4), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(8, 8), (4, 4), (None, None), (None, None)]

# LOOP 4
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (4, 4), (None, None)]

# LOOP 5
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (4, 4)]

# LOOP 6
   # Pop (4,4) from stack
   # p_node.val = 4, q_node.val = 4
   # 4 == 4 : True
   # right children: stack.append((p.right, q.right)) => (None, None) => stack is now [(8, 8), (None, None)]
   # left children: stack.append((p.left, q.left)) => (None, None) => stack is now [(8, 8), (None, None), (None, None)]

# LOOP 7
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8), (None, None)]

# LOOP 8
   # Pop (None, None) from stack
   # Both nodes are None, continue
   # stack is now [(8, 8)]

# LOOP 9
   # Pop (8,8) from stack
   # p_node.val = 8, q_node.val = 8
   # 8 == 8 : True
   # right children: stack.append((p.right, q.right)) => (9, 9) => stack is now [(9, 9)]
   # left children: stack.append((p.left, q.left)) => (6, 7) => stack is now [(9, 9), (6, 7)]

# LOOP 10
   # Pop (6,7) from stack
   # p_node.val = 6, q_node.val = 7
   # 6 == 7 : False
   # Return False, trees are not identical

# Function returns False, indicating the trees are not the same
