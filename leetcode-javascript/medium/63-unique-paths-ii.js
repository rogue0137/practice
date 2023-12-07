/**
 * https://leetcode.com/problems/unique-paths-ii/
 * @param {number[][]} obstacleGrid
 * @return {number}
 * DFS approach => too slow
 */
const uniquePathsWithObstaclesDFS = function(obstacleGrid) {
    let uniquePaths = 0;

    const colLen = obstacleGrid.length;
    const rowLen = obstacleGrid[0].length;

    const move = function(grid, col, row) {
        // are we still in bounds?
        if (col >= colLen || row >= rowLen) {
            return;
        }
        
        const currSpace = grid[col][row];
        
        // check for obstacle
        if (currSpace === 1) {
            return;
        }
        // check if we are at the end
        // can the end be blocked? do I have to check that it's a 0? yes, see above
        if (col === colLen - 1 && row === rowLen - 1) {
            uniquePaths += 1;
            return;
        }

        // check if we can go right
        move(grid, col + 1, row);

        // check if we can go down
        move(grid, col, row + 1);
    }

    move(obstacleGrid, 0, 0);

    return uniquePaths;
};

/**
 * https://leetcode.com/problems/unique-paths-ii/
 * @param {number[][]} obstacleGrid
 * @return {number}
 * Dynamic programming approach
 */
const uniquePathsWithObstaclesDP = function(obstacleGrid) {
    const colLen = obstacleGrid.length;
    const rowLen = obstacleGrid[0].length;

    // create a new grid to store the number of paths to each space
    let newGrid = Array(colLen).fill(0).map(() => Array(rowLen).fill(0));

    // set the first space to 1 if it is not an obstacle
    if (obstacleGrid[0][0] === 0) {
        // so far we have one pathway
        newGrid[0][0] = 1;
    }

    // set the first column
    for (let col = 1; col < colLen; col++) {
        if (obstacleGrid[col][0] === 0) {
            // if the space is not an obstacle, 
            // then the number of paths is the same as the space above it
            newGrid[col][0] = newGrid[col - 1][0];
        }
    }
   
    // set the first row
    for (let row = 1; row < rowLen; row++) {
        if (obstacleGrid[0][row] === 0) {
            // if the space is not an obstacle,
            // then the number of paths is the same as the space to the left of it
            newGrid[0][row] = newGrid[0][row - 1];
        }
    }

    // fill the rest of the matrix
    // start at col 1 and row 1 because we already filled the first row and column
    /**
     * Visual representation: 
     * - F is filled
     * - S is start here
     * - E is for empty since we have not filled these yet
     * [  
        * [F, F, F],
        * [F, S, E],
        * [F, E, E],
     * ]
     */

    for (let col = 1; col < colLen; col++) {
        for (let row = 1; row < rowLen; row++) {
            if (obstacleGrid[col][row] == 0) {
                const above = newGrid[col - 1][row];
                const left = newGrid[col][row - 1];
                newGrid[col][row] = above + left;
            }
        }
    }

    const accumulatedPaths = newGrid[colLen - 1][rowLen - 1];

    return accumulatedPaths
};

/**
 * Grid: 2D array, m x n
 * 
 * Example: [
 *  [0,0,0],
 *  [0,1,0],
 *  [0,0,0
 * ] 
 * 
 * Robot starts at grid[0][0].
 * Robot wants to get to grid[m.len - 1][n.len - 1].
 * Robot can only move down (m - 1) or right (n - 1).
 * 
 * 1 = obstacle
 * 0 = space
 * 
 * Robot cannot go through an obstacle. 
 * What are the unique paths the robot can take to get to the end?
 */
