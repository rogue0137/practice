# 677. Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.int = 0
        

    def insert(self, key: str, val: int) -> None:
        node = self
        for char in key:
            if char not in node.children:
                node.children[char] = MapSum()
            node = node.children[char]
            node.int += val  
        

    def sum(self, prefix: str) -> int:
        sum = 0
        node = self
        for char in prefix:
            if char not in node.children:
                return node.int
            node = node.children[char]
        
        return node.int

# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple",3], ["ap"], ["app",2], ["ap"]]

# sum when `apple` and `app` are words
# ROUND 1
    # node = []
    # char = 