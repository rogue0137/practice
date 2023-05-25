// const _ = require('lodash');

// function sayHello() {
//   console.log('Hello, World');
// }

// _.times(5, sayHello);

// Your previous Plain Text content is preserved below:

// input is a 2-D a


// Given a 2-D binary array (contains 0's and 1's), we want to output how many islands there are in the Array. An island is a grouping of 1's that are connected to each other adjacently but not diagonally.


// [
//   [ 0, 0, 1, 1 ],
//   [ 0, 0, 1, 1 ],
//   [ 1, 1, 0, 0 ]
// ]

//  => 2 islands

//  [
//   0, 0, 1,
//   0, 1, 0, 
//   1, 0, 0, 
// ] => 3 islands

// [
//   [ 1, 0, 1],
//   [ 0, 0, 0],
//   [ 1, 0, 1]
// ] => 4 islands
const assert = require('assert');


// basic function
const getNumOfIslands = (input) => {
  // iterate through the matrix
  // row
  const rowLength = input.length;
  if (rowLength === 0) {
    return 0;
  }
  // column
  const columnLength = input[0].length;
  // specific point

  let numOfIslands = 0;
  const seen = 'X';

  const traverseIsland = (input, row, rowLength, column, columnLength) => {
    const seen = 'X'
    // this updates #ofIslands
    // up or down
    // once checked, we need a way to mark it as seen, "X"
    // if row > 0, then we can go up
    if (row > 0) {
      if (input[row - 1][column] === 1) {
        input[row - 1][column] = seen;
        traverseIsland(input, row - 1, rowLength, column, columnLength, seen);
      } else {
        input[row - 1][column] = seen;
      }
  
    }
    // if row is < rowLength we can go down
    if (row < rowLength - 1) {
      if (input[row + 1][column] === 1) {
        input[row + 1][column]= seen;
        traverseIsland(input, row + 1, rowLength, column, columnLength, seen);
      } else {
        input[row + 1][column]= seen;
      }
    }
    // left or right
    // once checked, we need a way to mark it as seen, "X"
    // if column > 0, then we can go left
    if (column > 0) {
      if (input[row][column - 1] === 1) {
        input[row][column - 1]= seen;
        traverseIsland(input, row, rowLength, column - 1, columnLength, seen);
      } else {
        input[row][column - 1] = seen;
      }
    }
    // if column < columnLength, then we can go right
    if (column < columnLength - 1) {
      if ( input[row][column + 1] === 1) {
        input[row][column + 1]= seen;
        traverseIsland(input, row, rowLength, column +1, columnLength, seen);
      } else {
        input[row][column + 1] = seen;
      }
    }
  }

  // console.log(input);
  for (let row = 0; row < rowLength; row++) {
    for (let column = 0; column < columnLength; column++) {
      const possibleIsland = input[row][column]; // 3. [2][0] = 1 2. [1][0] = 0 1. [0][0] = 0
      // save #ofIslands
      if (possibleIsland === seen) { 
        continue;
      } else {
        if (possibleIsland === 1) { // 3. [2][0]= 1
         numOfIslands += 1;
         input[row][column] = seen;
         traverseIsland(input, row, rowLength, column, columnLength);
         // console.log(input);
        } else {
          input[row][column] = seen; // 2. 'X' 1. 'X'
        }
      }
      // check "is this a 1 or 0", if "X" skip
      // once checked, we need a way to mark it as seen, "X"
      // if we see a 1, are there other ones next to it
    }
  }

  return numOfIslands;
  
}



const input1 = [
  [ 0, 0, 1, 1 ],
  [ 0, 0, 1, 1 ],
  [ 1, 1, 0, 0 ]
];


const input2 = [
  [0, 0, 1],
  [0, 1, 0], 
  [1, 0, 0], 
]; 

const input3 = [
  [ 1, 0, 1],
  [ 0, 0, 0],
  [ 1, 0, 1]
];

const input4 = [
  [ 0, 0, 0],
  [0, 0, 0]
];

const input5 = [];



// console.log(getNumOfIslands(input));
assert.equal(getNumOfIslands(input1), 2);
assert.equal(getNumOfIslands(input2), 3);
assert.equal(getNumOfIslands(input3), 4);
assert.equal(getNumOfIslands(input4), 0);
assert.equal(getNumOfIslands(input5), 0);
