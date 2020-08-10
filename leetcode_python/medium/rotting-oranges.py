# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/


# minimum number of minutes for all to rot
# 0 empty
# 1 fresh
# 2 rotten


# above, below, left, right
# if 0, ignore
# if 1, turn rotten and do more BFS
# if 2, do more BFS

class Solution:
    def rot_surroundings(self, grid, row, col, len_rows, len_cols):


    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use queue