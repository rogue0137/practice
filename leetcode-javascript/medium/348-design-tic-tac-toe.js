/**
 * Initialize your data structure here.
 * @param {number} n
 */
const TicTacToe = function(n) {
    this.board = new Array(n);
    this.size = n;
    for (let i = 0; i < n; i++) {
        this.board[i] = new Array(n);
    }
};

/**
 * Player {player} makes a move at ({row}, {col}).
 @param row The row of the board.
 @param col The column of the board.
 @param player The player, can be either 1 or 2.
 @return The current winning condition, can be either:
 0: No one wins.
 1: Player 1 wins.
 2: Player 2 wins.
 * @param {number} row
 * @param {number} col
 * @param {number} player
 * @return {number}
 */
TicTacToe.prototype.move = function(row, col, player) {
    const xOrO = player === 1 ? 'X' : 'O';
    this.board[row][col] = xOrO;
    // is the whole row mentioned above X or O
    if (
        this.board[row][0] === xOrO &&
        this.board[row][1] === xOrO &&
        this.board[row][2] === xOrO
    ) {
        return player;
    }
    // is the whole col mentioned above X or O
    if (
        this.board[0][col] === xOrO &&
        this.board[1][col] === xOrO &&
        this.board[2][col] === xOrO
    ) {
        return player;
    }
    // is the above placement part of a diagonal?
    const sizeMinusOne = this.size - 1;

    // are touching boxes also X or O?
    // go down diagonally?
    let diagonal = [row, col];
    let plusOrMinusSquare;
    if (
        ( row === 0 && col === 0 ) ||
        ( row === 0 && col === sizeMinusOne )
    ) {
        let down = 0;
        plusOrMinusSquare = col === 0 ? 1 : -1;
        while (down < sizeMinusOne) {
            diagonal = [row + 1, col + plusOrMinusSquare];
            if (this.board[diagonal[0][1]] !== xOrO) {
                break;
            }
            down++;
        }
        console.log(`go down diagonally`);
    } // go up diagonally?
    if (
        ( row === sizeMinusOne && col === 0 ) ||
        ( row === sizeMinusOne && col === sizeMinusOne)
    ) {
        let up = 0;
        plusOrMinusSquare = row === 0 ? 1 : -1;
        while (up < sizeMinusOne) {
            diagonal = [row - 1, col + plusOrMinusSquare ];
            console.log(`diagonal: ${diagonal}`);
            if (this.board[diagonal[0][1]] !== xOrO) {
                console.log(`about to break`);
                break;
            }
            up++;
        }
        if (up === sizeMinusOne) {
            return player;
        }

    } // am I in the middle?
    if ( row === sizeMinusOne/2 && col === sizeMinusOne/2 ) {
        console.log(`in the middle`);
    }
    return 0;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */

const board = new TicTacToe(3);
console.log(board);

// Test 1
//     ["TicTacToe","move","move","move","move","move","move","move"]
//     [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
// console.log(board.move(0,0,1));
// console.log(board.move(0,2,2));
// console.log(board.move(2,2,1));
// console.log(board.move(1,1,2));
// console.log(board.move(1,0,2));
// console.log(board.move(2,1,1));
// console.log(board);


// TEST 2
console.log(board.move(0,0,1));
console.log(board.move(0,2,2));
console.log(board.move(2,2,1));
console.log(board.move(1,1,2));
console.log(board.move(2,0,2));
console.log(board.move(1,0,2));
console.log(board.move(2,1,1));
console.log(board);