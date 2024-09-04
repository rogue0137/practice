# https://leetcode.com/problems/same-tree/description/

# These solutions are specifically only showing NON-recursive (in this case queue) approaches.
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
