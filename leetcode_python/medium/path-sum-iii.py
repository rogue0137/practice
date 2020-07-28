# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(
            self,
            node: TreeNode,
            leftover_sum: int, 
            list_of_nodes: List[int],
            list_of_paths: List[List[int]]):
        if not node:
            return

        # append curr val
        list_of_nodes.append(node.val)
        print(f'leftover_sum: {leftover_sum}')
        # REQUIREMENT
        if leftover_sum - node.val == 0:
            list_of_paths.append(list_of_nodes)
        else:
            self.DFS(node.left, leftover_sum, list_of_nodes, list_of_paths)
            self.DFS(node.left, leftover_sum, list_of_nodes, list_of_paths)
        list_of_nodes.pop()

    def pathSum(self, root: TreeNode, sum: int) -> int:
        list_of_paths = []
        self.DFS(root, sum - root.val, [], list_of_paths)
        print(list_of_paths)
        return len(list_of_paths)