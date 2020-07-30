# BFS
# pre-order
def BFS(self, node, tree_order):
    if node:
        tree_order.append(node.val)
        self.BFS(node.left, tree_order)
        self.BFS(node.right, tree_order)
    return tree_order

def preorderTraversal(self, root):
    tree_order = []
    self.BFS(root, tree_order)
    return tree_order

# BFS
# in-order
def BFS(self, node, tree_order):
    if node.left:
        self.BFS(node.left, tree_order)
    if node:
        tree_order.append(node.val)
    if node.right:
        self.BFS(node.right, tree_order)
    return tree_order


def inorderTraversal(self, root):
    tree_order = []
    if root:
        self.BFS(root, tree_order)
    return tree_order

# BFS
# post-order
def BFS(self, node, tree_order):
    if node.left:
        self.BFS(node.left, tree_order)
    if node.right:
        self.BFS(node.right, tree_order)
    if node:
        tree_order.append(node.val)
    return tree_order

def postorderTraversal(self, root):
    tree_order = []
    if root:
        self.BFS(root, tree_order)
    return tree_order

# BFS
# level-order

def BFS(self, node, level, tree_order):
    pass

def levelorderTraversal(self, root):
    tree_order = []
    if root:
        self.BFS(root, 1, tree_order)
    return tree_order

