# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create grid
        # m = total columns
        # n = total rows
        grid = [[0]* m for _ range(n)]

        # fill out first column, column at index 0
        for i in range(n):
            print(f'i: {i}')
            grid[i][0] = 1
     
        # fill out first row, row at index 0
        for j in range(m):
            grid[0][j] = 1

        # Starting from cell(1,1) fill up the values
        # i.e. From above and left.
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        # Return value stored in rightmost bottommost cell. That is the destination.      
        return grid[n-1][m-1]

# Runtime: 56 ms, faster than 8.09% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 30.46% of Python3 online submissions for Unique Paths.