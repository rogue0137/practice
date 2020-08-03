# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
TREE/GRAPH LOOKS LIKE THIS

L1:                    1
                    /  |  \
L2:                3   2   4
                  / \
L3:              5   6
"""

class Solution:
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

# starting queue: [1]
# starting levels: []
# starting level = 0
# ROUND 1
    # queue exists
    # append level --> [ [] ]
    # level_len --> 1
    # for i in range(1):
        # node --> 1
        # queue now []
        # add to levels --> levels[0].append(1) --> levels = [ [1]]
        # node.children are [3, 2, 4]
        # updated queue --> [3, 2, 4]
    # level -> 1
# ROUND 2
    # queue exists
    # append level --> [ [1], []]
    # level_len --> 3
    # for i in range(3):
        # FIRST ITERATION
            # node --> 4
            # queue now [3, 2]
            # add to levels --> levels[1].append(4) --> levels = [ [1], [4]]
            # no children, don't update queue
        # SECOND ITERATION
            # node --> 2
            # queue now [3]
            # add to levels --> levels[1].append(2) --> levels = [ [1], [4, 2]]
            # no children, don't update queue
        # THIRD ITERATION
            # node --> 3
            # queue now []
            # add to levels --> levels[1].append(3) --> levels = [ [1], [4, 2, 3]]
            # children = [5, 6]
            # updated queue --> [5, 6]
    # level -> 2
# ROUND 3
    # queue exists
    # append level --> [ [1], [4, 2, 3], []]
    # level_len -> 2
    # for i in range(2)
        # FIRST ITERATION
            # node --> 6
            # queue now [5]
            # add to levels --> levels[2].append(6) --> levels = [ [1], [4, 2, 3], [6]]
            # no children, don't update queue
        # SECOND ITERATION
            # NODE --> 5
            # queue now []
            # add to levels --> levels[2].append(5) --> levels = [ [1], [4, 2, 3], [6, 5]]
            # no children, don't update queue
# ROUND 4
    # queue no longer exist
    # return levels --> [ [1], [4, 2, 3], [6, 5]]

# Runtime: 44 ms, faster than 99.12% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 15.7 MB, less than 39.58% of Python3 online submissions for N-ary Tree Level Order Traversal.
