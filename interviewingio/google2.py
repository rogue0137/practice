
# Given an org chart as a tree, each node is an employee.  Each node has a personal happiness score (the greater the integer, the greater the happiness).  Each manager (node with children) has an average happiness: the average happiness of all reports and him/herself.  Compute the average happiness of all nodes in the tree.


# DFS
# root
# children
# append(value)
# avg(values)
class TreeNode
from typing import List




# Input
#         3 --> 5.5
#  3--> 3     4 --> 4         7 --> 7.6
#                            8 --> 8  8 --> 8
# Output


# everyone has a happiness and an average happiness

# [ 3, 3, 4, 8, 8, 7  ]

# ```
# .personal_happiness: 7
# .avg_happiness: 7.6
# .children [ 8, 8]
# .total_happiness -- this is all happiness below me with me
# .total_reports -- count of all reports below me and with me
# ``` 
    
class Solution:
    def DFS(self, node: TreeNode):
        

        # REQUIREMENT: 
        # avg of node plus all children
        for child in node.children:
            self.DFS(child)
            total_happiness += child.total_happiness
            total_reports += child.total_reports
        total_happiness += node.personal_happiness
        total_reports += 1
        node.total_happiness = total_happiness
        node.total_reports = total_reports
        
    
        node.avg_happiness = float(node.total_happiness) / node.total_reports
        

    def calculate_average_happiness(self, root: TreeNode) -> int: 
        tree_happiness = []
        self.DFS(root, tree_happiness, ) # 3
        return root 
