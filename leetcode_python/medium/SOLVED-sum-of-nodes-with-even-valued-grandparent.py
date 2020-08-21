# 1315. Sum of Nodes with Even-Valued Grandparent
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    def DFS(self, node, granchildren_sum):
        if node:
            self.DFS(node.right, granchildren_sum)
            self.DFS(node.left, granchildren_sum)
            is_even = node.val % 2 == 0
            if is_even:
                new_sum = 0
                if node.left:
                    if node.left.left:
                        new_sum += node.left.left.val
                    if node.left.right:
                        new_sum += node.left.right.val
                if node.right:
                    if node.right.left:
                        new_sum += node.right.left.val
                    if node.right.right:
                        new_sum += node.right.right.val
                granchildren_sum.append(new_sum)

        return granchildren_sum

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        granchildren_sum = []
        self.DFS(root, granchildren_sum)
        total_sum = sum(granchildren_sum)
        return total_sum

# Runtime: 100 ms, faster than 94.09% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 16.9 MB, less than 99.61% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

# ITERATIVE SOLUTION
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        grandchildren_sum = 0

        parent = None # root does not have parent
        grandparent = None # root does not have grandparent

        first_value_in_stack = (root, parent, grandparent)
        stack = [ first_value_in_stack ]

        # PRE-ORDER
        # TOP --> BOTTOM
        while stack:
            node, parent, grandparent = stack.pop()

            if grandparent and grandparent % 2 == 0:
                grandchildren_sum += node.val

            if node.left:
                stack.append( (node.left, node.val, parent) )

            if node.right:
                stack.append( (node.right, node.val, parent) )

        return grandchildren_sum

# Runtime: 112 ms, faster than 54.77% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 17.2 MB, less than 59.91% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.