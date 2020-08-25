### DEQUE: if you just want a queue or a double-ended queue as a datastructure, use `collections.deque`.

"""
TREE/GRAPH LOOKS LIKE THIS

L1:                    1
                      / \
L2:                  2   3
                    /  / | \
L3:                4  5  6  7
                        / \
L4:                    8   9

TREE INPUT WILL BE REPRESENTED AS:


YOU WANT TO PRINT
Level 1: 1
Level 2: 2,3
Level 3: 4, 5, 6, 7
Level 4: 8, 9
"""
from typing import List
from collections import deque


def get_levels(tree:List[List[int]]): 
    graph_len = len(tree)

    # array to store level of each node  
    level = [None] * graph_len  
    marked = [False] * graph_len
  
    # create a queue
    que = deque()
  
    # enqueue element x
    que.append(graph[0])  
  
    # do until queue is empty  
    while len(que) > 0: 
        print('here')
  
        # get the first element of queue  
        x = que.popleft()  
  
    # display all nodes and their levels  
    for i in range(graph_len): 
        print(f'{level[i]} is at level: {i}') 

if __name__ == '__main__':
  
    # CREATE TREE
    levels = 4
    tree = [[] for i in range(levels)]
    print(f'graph created: {tree}')

    tree[0].append(1)
    tree[1].append(2)
    tree[1].append(3)
    tree[2].append(4)
    tree[2].append(5)
    tree[2].append(6)
    tree[2].append(7)
    tree[3].append(8)
    tree[3].append(9)
    print(f'graph filled: {tree}')
  
    # call levels function with source as 0  
    # get_levels(graph) 
