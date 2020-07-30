# BFS
    # uses queue
    # good for shortest path
    # for binary tree: level order
# DFS
    # uses stack
    # great for exploring all paths, ex. games, puzzles
    # for binary tree: inorder, preorder, postorder

# "Top-down" solution
# Visit node, add value, pass values to children
# Ex. preorder
# QUESTIONS TO DETERMINE IF TOP-DOWN IS A SOLUTION:
#  Can you determine some parameters to help the node know its answer?  YES
# Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children? YES

# "Bottom-up" solution
# visit children, add value, pass values up back to parent
# Ex. post-order
# QUESTIONS TO DETERMINE IF BOTTOM-UP IS A SOLUTION:
# For a node in a tree, if you know the answer of its children, can you calculate the answer of that node? YES


# PRE-ORDER
# "top-down"
# stack and array

# binary tree recursive solution
def BFS(node, tree_order):
    if node:
        tree_order.append(node.val)
        BFS(node.left, tree_order)
        BFS(node.right, tree_order)
    return tree_order

def preorderTraversal(root):
    tree_order = []
    BFS(root, tree_order)
    return tree_order


# binary tree iterative solution
def BFS_preorder(node):
    if not node:
        return []
    # NOTE:
    # append whole node to stack
    # only append node.val to preorder_array
    stack, preorder_array = [node], []

    while stack:
        node = stack.pop()
        if node:
            preorder_array.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return preorder_array

# BFS for max depth 
def BFS(node, depth):
    # visit node
    if not node:
        return 0

    # go onto it's children
    left_depth = BFS(node.left)
    right_depth = BFS(node.right)

    # pass value from original node onto children
    max_depth = max(left_depth, right_depth) + 1
    return max_depth


# IN-ORDER
# stack, array

# binary tree recursive solution
def BFS(node, tree_order):
    if node.left:
        BFS(node.left, tree_order)
    if node:
        tree_order.append(node.val)
    if node.right:
        BFS(node.right, tree_order)
    return tree_order

def inorderTraversal(root):
    tree_order = []
    if root:
        BFS(root, tree_order)
    return tree_order

# binary tree iterative solution
def BFS_inorder(node):
    if not node:
        return []
    stack, preorder_array = [], []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        preorder_array.append(node.val)
        node = node.right
    return preorder_array


# POST-ORDER
# bottom-down
# stack, array

# binary tree recursive solution
def BFS(node, tree_order):
    if node.left:
        BFS(node.left, tree_order)
    if node.right:
        BFS(node.right, tree_order)
    if node:
        tree_order.append(node.val)
    return tree_order

def postorderTraversal(root):
    tree_order = []
    if root:
        BFS(root, tree_order)
    return tree_order

# binary tree iterative solution
# COME BACK TO!!!
# REWATCH VIDEO: https://leetcode.com/articles/binary-tree-postorder-traversal/
def BFS_postorder(node):
    stack, postorder_array = [], []

    # set up the stack?
    while node or stack:
        while node:
            # this basically makes it so that 
            # you never append node.left, but only
            # when it's the "node" of a node.right child
            if node.right:
                stack.append(node.right)
            stack.append(node)
            print(f'stack: {stack}')
            node = node.left
        
        node = stack.pop()

        # checking that the node you popped
        # is leftmost
        # NOT THE LEFTMOST
        if stack and node.right == stack[-1]:
            print(f'resetting node')
            # reassign the node to node.right
            # swap left and right
            stack[-1] = node
            node = node.right
        # THE LEFTMOST
        else:
            postorder_array.append(node.val)
            print(f'post_order: {postorder_array}')
            node = None
            
    return postorder_array


# LEVEL-ORDER
# queue, array

# binary tree recursive solution
# does not work in leetcode, CHECK
def BFS(node, level, tree_order):
    if node:
        if len(tree_order) == level:
            tree_order.append([])
        tree_order[level].append(node)
        if node.left:
            BFS(node.left, level + 1, tree_order)
        if node.right:
            BFS(node.right, level + 1, tree_order)
    return tree_order

def levelorderTraversal(root):
    tree_order = []
    if root:
        BFS(root, 0, tree_order)
    return tree_order

# binary tree iterative solution
from collections import deque
def bfs_level_order(node):
    levels = []
    if not node:
        return levels
    level = 0
    queue = deque([node])

    while queue:
        levels.append([])
        level_len = len(queue)
        for i in range(level_len):
            node = queue.popleft()
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1

    return levels

