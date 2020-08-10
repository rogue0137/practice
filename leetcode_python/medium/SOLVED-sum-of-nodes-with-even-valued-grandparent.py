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