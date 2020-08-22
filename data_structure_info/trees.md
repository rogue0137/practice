# Trees

**Table of Contents**
- ["Top-down"](#top-down)
- ["Bottom-up"](#bottom-up)
- [BFS](#bfs)
    - [level-order cheatsheet](#level-order)
- [DFS](#dfs)
    - [pre-order cheatsheet](#pre-order)
    - [in-order cheatsheet](#in-order)
    - [post-order cheatsheet](#post-order)
- [BFS vs DFS Diagram](#bfs-vs-dfs-diagram)
- [Summary Diagrams](#summary-diagrams)

## Top-down
- Denotes recursive solution
- Visit node, add value, pass values to children
    - Ex. [pre-order](#pre-order)
- QUESTIONS TO DETERMINE IF TOP-DOWN IS A SOLUTION:
    - Can you determine some parameters to help the node know its answer? `YES`
    - Can you use these parameters and the value of the node itself to determine what should be the parameters passed to its children? `YES`

## Bottom-up
- Denotes recursive solution
- Visit children, add value, pass values up back to parent
    - Ex. [post-order](#post-order)
- QUESTIONS TO DETERMINE IF BOTTOM-UP IS A SOLUTION:
    - For a node in a tree, if you know the answer of its children, can you calculate the answer of that node? `YES`

## BFS
- breadth-first search
- uses queue (double-endeded queue `deque` in python)
- good for:
    - shortest path
    - anything to do with levels
- commonly associated with:
    - [level order](#level-order)

### LEVEL-ORDER
- uses: queue, array
- suitable for both binary and N-ary trees

#### BFS Leetcode problems
- [EASY: Find All the Lonely Nodes](https://leetcode.com/problems/find-all-the-lonely-nodes) -- [my solution](../../leetcode_python/easy/SOLVED-find-all-the-lonely-nodes.py)
- [MEDIUM: Binary Tree Level Order Problem](https://leetcode.com/problems/binary-tree-level-order-traversal/) -- [my solution](../../leetcode-python/medium/SOLVED-binary-tree-order-traversal.py)
- [MEDIUM: N-ary Tree Level Order Problem](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) -- [my solution](../../leetcode-python/medium/SOLVED-n-ary-tree-order-traversal.py)
- [MEDIUM: Max depth DFS problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [MEDIUM: Number of Islands](https://leetcode.com/problems/number-of-islands/) - [my solution: BFS bottom solution](../../leetcode-python/medium/SOLVED-number-of-islands.py)

_not BFS but good to know so you can make sure you understand it_: [EASY: SYMMETRIC TREE](https://leetcode.com/problems/symmetric-tree/) -- [my solution](../../leetcode_python/easy/SOLVED-symmetric-tree.py)


#### binary tree recursive solution
(does not work in leetcode, CHECK)
```python
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
```

#### binary tree iterative solution
```python
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
```

#### N-ary tree iterative solution
```python
def levelOrder(self, node: 'Node') -> List[List[int]]:
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
                queue.extend(node.children)
            level += 1
        return levels
```

## DFS
- depth first search
- uses stack
- good for
    - exploring all paths, ex. games, puzzles
- commonly associated with:
    - [inorder](#inorder)
    - [preorder](#preorder)
    - [postorder](#postorder)

#### Uncatecategorized DFS Leetcode problems
- [MEDIUM: Number of Islands](https://leetcode.com/problems/number-of-islands/) - [my solution: top is DFS](../../leetcode-python/medium/SOLVED-number-of-islansd.py)

### PRE-ORDER
- "top-down" approach when executed recursively
- uses: stack and array
- suitable for both binary and N-ary trees

#### Pre-order Leetcode Problems

- [MEDIUM: Binary Tree Preorder Problem](https://leetcode.com/problems/binary-tree-preorder-traversal/) -- [my solution](../../leetcode-python/medium/SOLVED-binary-tree-preorder-traversal.py)
- [MEDIUM: Path Sum II](https://leetcode.com/problems/path-sum-ii/) -- [my solution](../../leetcode-python/medium/SOLVED-path-sum-ii.py)

#### Pre-order binary tree recursive solution
```python
def DFS(node, tree_order):
    if node:
        tree_order.append(node.val)
        DFS(node.left, tree_order)
        DFS(node.right, tree_order)
    return tree_order

def preorderTraversal(root):
    tree_order = []
    DFS(root, tree_order)
    return tree_order
```

#### binary tree iterative solution

```python
def DFS_preorder(node):
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
```

#### N-ary tree recursive solution

```python
""" 
Assuming the Following definition of Node:
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


def preorder(node: Node) -> order:List[int]:
    order = []
    
    if node:
        order.append(node.val)
        children_node = node.children
        if children_node:
            for child in children_node:
                values_of_child = preorder(child)
                
                order = order + values_of_child
              
    return order
```

#### N-ary tree iterative solution

```python
""" 
Assuming the Following definition of Node:
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


def preorder(node: Node) -> order:List[int]:
    order = []
    
    if node is None:
        return order

    stack =  [node]
    while stack:
        node = stack.pop()
        order.append(node.val)
        # appending in reverse order will ensure that
        # we pop them in L -> R order; see below
        stack.extend(node.children[::-1])
    return order

"""
When appending the children of 1, the stack will look like:
stack = [3, 2]
This way we pop 2 first and deal with it's child (4) before we
look at anything on the right (3).

TREE/GRAPH LOOKS LIKE THIS

L1:                    1
                      / \
L2:                  2   3
                    /  / | \
L3:                4  5  6  7
"""
```

## IN-ORDER
- depth first approach
- uses: stack and array
- suitable for binary trees

### In-order: Leetcode Porblems

- [MEDIUM: Binary Tree In-order Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/) -- [my solution](../../leetcode-python/medium/binary-tree-inorder-traversal.py)

### In-order Binary Tree
#### binary tree recursive solution

```python
def DFS(node, tree_order):
    if node.left:
        DFS(node.left, tree_order)
    if node:
        tree_order.append(node.val)
    if node.right:
        DFS(node.right, tree_order)
    return tree_order

def inorderTraversal(root):
    tree_order = []
    if root:
        DFS(root, tree_order)
    return tree_order
```

#### binary tree in-order iterative solution
```python
def DFS_inorder(node):
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
```

## POST-ORDER
- depth first approach
- "bottom-up" approach when executed recursively
- uses: stack, array
- suitable for both binary and N-ary trees

### Post-Order Leetcode Problems
- [EASY: Leaf Similar Trees ](https://leetcode.com/problems/leaf-similar-trees) -- [my solution](../../leetcode_python/easy/SOLVED-leaf-similar-trees.py)
- [EASY: Maximum depth of a binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) -- [my solution: top is DFS](../../leetcode_python/easy/SOLVED-maximum-depth-of-binary-tree.py)
- [EASY: Minimum depth of a binary tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/) -- [my solution](../../leetcode_python/easy/SOLVED-minimum-depth-of-a-binary-tree.py)
- [MEDIUM: Sum of Nodes with Even Valued Grandparents](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) -- [my solution](../../leetcode-python/medium/SOLVED-sum-of-nodes-with-even-valued-grandparent.py)
- [MEDIUM: House Robber III](https://leetcode.com/problems/house-robber-iii/) - [my solution](../../leetcode-python/medium/SOLVED-house-robber-iii.py)
- [HARD: Binary tree postorder problem](https://leetcode.com/problems/binary-tree-postorder-traversal/) -- [my solution](../leetcode_python/hard/SOLVED-binary-tree-postorder-traversal.py)
- [HARD: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) -- [my solution](../../leetcode_python/hard/SOLVED-binary-tree-maximum-path-sum.py)
- [HARD: Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) -- [my solution](../../leetcode_python/hard/SOLVED-binary-tree-postorder-traversal.py)

### Post-order Binary Tree
#### binary tree recursive solution

```python
def DFS(node, tree_order):
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
        DFS(root, tree_order)
    return tree_order
```

#### binary tree iterative solution

```python
def BFS_postorder(node):
    stack, postorder_array = [], []

    while node or stack:
        # set up the stack
        while node:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            node = node.left
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
```
#### N-ary tree recursive solution
```python
""" 
Assuming the Following definition of Node:
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


def postorder(node: Node) -> order:List[int]:
    order = []
    if node:
        children = node.children
        if children:
            for child in children:
                value_of_child = postorder(child)
                order = order + value_of_child
            order.append(node.val)
    return order
```

#### N-ary tree iterative solution
```python
""" 
Assuming the Following definition of Node:
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


def postorder(node: Node) -> order:List[int]:
    order = []
    if node is None:
        return order
    
    stack= [node]
    
    while stack:
        node = stack.pop()
        if node:
            order.append(node.val)
        for child in node.children:
            stack.append(child)
        """
        Instead of the for loop:
        if node.children:
            stack.extend(node.children)
        """
    reversed_order = order[::-1]
    return reversed_order
```


#### BFS for max depth using recursion

TO-DO



## BFS vs DFS as Diagram
|   | BFS  |  DFS |
|-:|:-:|:-:|
| **Helpful Data Structure** |  Queue | Stack  |
| **Helpful algorithms**  |  Level order | Inorder  |
|   |   | Preorder  |
|   |   | Postorder |
| **Good for**  | Shortest Path  | Get all paths  |
|   |   |   | Anything levels  |

## Summary Diagrams

### Binary Trees

![Leetcode Binary Tree Traversal Image](https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/Figures/145_transverse.png)

### N-ary Trees
![Image of N-ary Tree Traversal](../images/N-ary_Tree_Traversal.png)