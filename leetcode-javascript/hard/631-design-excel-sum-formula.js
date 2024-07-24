// https://leetcode.com/problems/design-excel-sum-formula/
const assert = require('assert');

class Excel {
    constructor(height, width) {
        this.height = height; // number of rows
        this.width = width; // number of columns
        this.spreadsheet = new Array(height).fill(0).map( 
            () => new Array(width).fill(0)
        );
    }

    set(row, column, value) {
        this.spreadsheet[row][column] = value;
    }

    get(row, column) {
        return this.spreadsheet[row][column];
    }

    sum(row, column, fieldsToBeSummed) {
        // This sum formula should exist until this cell is overlapped by 
        // another value or another sum formula.
    }
}

const excelSheet = new Excel(3, 3);
assert(excelSheet.height === 3);
assert(excelSheet.width === 3);
/** When comparing arrays or objects, JavaScript doesn't perform a deep comparison.
* Instead, it checks whether the two variables refer to the exact same object,
* not whether their contents are identical. Thus, instead of using `===` to compare
* arrays, use `assert.deepStrictEqual()` to perform a deep comparison.
**/
const expectedMatrix = [[0,0,0],[0,0,0],[0,0,0]];
assert.deepStrictEqual(excelSheet.spreadsheet, expectedMatrix);
