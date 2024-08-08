# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, node: TreeNode) -> bool:
        queue = []
        queue.append(node)
        queue.append(node)
        while len(queue) > 0:
            node1 = queue.pop()
            node2 = queue.pop()
            if node1 == None and node2 == None:
                continue
            if node1 == None or node2 == None:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True

# [1,2,2,null,3,null,3] -> False
#    1
#   / \
#  2   2
#   \   \
#    3   3

# ROUND 1
    # queue created
    # append root twice -> [1, 1]
    # len of q is > 0
        # node1 -> 1
        # node 2 -> 1
        # don't meet any of the if requirements
        # append nodes: [2, 2, 2, 2]
# ROUND 2
    # len of q is > 0 -> [2, 2, 2, 2]
        # node1 -> 2
        # node2 -> 2
        # don't meet any of the if requirements
        # append nodes: [2, 2, 3, None, 4, None]
# ROUND 3
    # len of q is > 0 -> [2, 2, 3, None, 4, None]
        # node1 -> None
        # node2 -> 4
        # node1 is None, return False

#[1,2,2,3,4,4,3] -> True
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# ROUND 1
    # queue created
    # append root twice -> [1, 1]
    # len of q is > 0
        # node1 -> 1
        # node 2 -> 1
        # don't meet any of the if requirements
        # append nodes: [2, 2, 2, 2]
# ROUND 2
    # len of q is > 0 -> [2, 2, 2, 2]
        # node1 -> 2
        # node2 -> 2
        # don't meet any of the if requirements
        # append nodes: [2, 2, 3, 3, 4, 4]
# ROUND 3
    # len of q is > 0 -> [2, 2, 3, 3, 4, 4]
        # node1 -> 4
        # node2 -> 4
        # don't meet any of the if requirements
        # these nodes don't have any children so append nothing
# ROUND 4
    # len of q is > 0 -> [2, 2, 3, 3]
        # node1 -> 3
        # node2 -> 3
        # don't meet any of the if requirements
        # these nodes don't have any children so appendn nothing
# ROUND 4
    # len of q is > 0 -> [2, 2]
        # node1 -> 2
        # node2 -> 2
        # don't meet any of the if requirements
        # append nodes: [3, 3, 4, 4]
# ROUND 5 
    # len of q is > 0 -> [3, 3, 4, 4]
        # node1 -> 4
        # node2 -> 4
        # don't meet any of the if requirements
        # these nodes don't have any children so append lots of Nones, which all cancel each other out
# ROUND 6
    # len of q is > 0 -> [3, 3]
        # node1 -> 3
        # node2 -> 3
        # don't meet any of the if requirements
        # these nodes don't have any children so append lots of Nones, which all cancel each other out
    # len of q is 0 so exit and return True

# Runtime: 40 ms, faster than 45.37% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 14.1 MB, less than 9.87% of Python3 online submissions for Symmetric Tree.
