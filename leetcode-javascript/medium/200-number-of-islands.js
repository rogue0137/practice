/**
 * @param {character[][]} grid
 * @return {number}
 * https://leetcode.com/problems/number-of-islands/
 */
const numIslands = function(grid) {
    // create a count variable
    let numberOfIslands = 0;

    // check for empty grid
    if (grid.length === 0) {
        return numberOfIslands;
    }

    const columnLength = grid.length;
    const rowLength = grid[0].length;

    // Set up directions we can move
    const up = [-1, 0];
    const down = [1, 0];
    const left = [0, -1];
    const right = [0, 1];
    const directions = [up, down, left, right];

    // create a visited grid
    // don't need to put a value in the first fill() since
    // the map function will fill it when we get to it
    const visitedGrid = Array(grid.length).fill().map(
        () => Array(grid[0].length).fill(false)
    );

    // this function updates the visitedGrid so that when we're looping below
    // we don't unnecessarily visit spaces
    const visitSpaces = function (col, row) {
        // check that we're not outside the grid
        const isOutsideLeftBounds = col < 0;
        const isOutsideRightBounds = col >= columnLength;
        const isOutsideTopBounds = row < 0;
        const isOutsideBottomBounds = row >= rowLength;
        
        if (
            isOutsideBottomBounds || 
            isOutsideLeftBounds || 
            isOutsideRightBounds || 
            isOutsideTopBounds 
            ) {
                return;
            }
        
        // check that we haven't visited this space before
        const hasBeenVisited = visitedGrid[col][row];
        // confirm this space is not water, but an island
        const isWater = grid[col][row] === '0';

        if (hasBeenVisited || isWater) {
            return;
        }
        
        visitedGrid[col][row] = true;
        
        // use the directions array: [up, down, left, right] 
        for (let direction of directions) {
            visitSpaces(col + direction[0], row + direction[1])
        }
    }
    
    // go through the grid looking for islands
    for (let col = 0; col < columnLength; col++) {
        for (let row = 0; row < rowLength; row++) {
            // check that we're only visiting islands
            // check that we haven't visited this space before
            if (grid[col][row] === '1' && visitedGrid[col][row] === false) {
                numberOfIslands += 1;
                visitSpaces(col, row);
            }
        }
    }
    
    return numberOfIslands;
};

/**
 * Restate the problem:
 * 
 * Grid: m x n (col x row)
 * 
 * '1' = land
 * '0' = water
 * 
 * Give the # of islands.
 * 
 * Island
 *  - 1 or more connected lands
 */
