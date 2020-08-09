# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List


# DFS SOLUTION
def DFS(grid, row, col, len_rows, len_cols):
    if row < 0 or col <  0 or row >= len_rows or col >= len_cols or grid[row][col] != '1':
        return
    # set current spot to zero
    grid[row][col] = 0

    # get adjacent nodes
    above = row + 1
    below = row - 1
    right = col + 1
    left = col - 1

    # DFS
    DFS(grid, above, col, len_rows, len_cols)
    DFS(grid, below, col, len_rows, len_cols)
    DFS(grid, row, right, len_rows, len_cols)
    DFS(grid, row, left, len_rows, len_cols)

def DFSnumIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    len_rows = len(grid)
    len_cols = len(grid[0])

    island_counter = 0
    for row in range(len_rows):
        for col in range(len_cols):
            spot = grid[row][col]
            if spot == '1':
                DFS(grid, row, col, len_rows, len_cols)
                island_counter += 1

    return island_counter

# Runtime: 164 ms, faster than 53.80% of Python3 online submissions for Number of Islands.
# Memory Usage: 14.8 MB, less than 74.35% of Python3 online submissions for Number of Islands.

# BFS Solution
def BFSnumIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    # print(grid)
    len_rows = len(grid)
    len_cols = len(grid[0])

    island_counter = 0
    for i in range(len_rows):
        for j in range(len_cols):
            if grid[i][j] == '1':
                island_counter += 1
                grid[i][j] = 0 # set to 0 because it's been "visited"
                island_queue = []
                island_queue.append([i, j])
                while len(island_queue) > 0:
                    spot = island_queue.pop()
                    row = spot[0]
                    col = spot[1]

                    # diff areas
                    above = row - 1
                    below = row + 1
                    left = col - 1
                    right = col + 1

                    if above >= 0 and grid[above][col] == '1':
                        island_queue.append([above, col])
                        grid[above][col] = 0
                    if below < len_rows and grid[below][col] == '1':
                        island_queue.append([below, col])
                        grid[below][col] = 0
                    if left >= 0 and grid[row][left] == '1':
                        island_queue.append([row, left])
                        grid[row][left] = 0
                    if right < len_cols and grid[row][right] == '1':
                        island_queue.append([row, right])
                        grid[row][right] = 0

    # print(island_counter)
    return island_counter

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# DFS check
assert DFSnumIslands(grid1) == 1
assert DFSnumIslands(grid2) == 3
# BFS check
assert BFSnumIslands(grid1) == 1
assert BFSnumIslands(grid2) == 3
