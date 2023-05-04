/**
 * initialize your data structure here.
 */
var MaxStack = function() {
    // create stack
    this.stack = [];
    // enable max value and index
    this.maxVal = null;
    this.maxValIndex = null;

    // Use this function to 1) set max of original stack
    // 2) Reset max when items are removed
    this._setNewMax = function() {
        let currMax = this.stack[0];
        let currMaxIndex = 0;

        // iterate through all indexes in stack
        // if something is equal to or greater, reset the
        // curMax and currMax Index
        for (let i = 0; i < this.stack.length; i++){
            let currVal = this.stack[i];
            if (currVal >= currMax) {
                currMax = currVal;
                currMaxIndex = i;
            }
        }

        // set values to the object
        this.maxVal = currMax;
        this.maxValIndex = currMaxIndex;
    }
};

/**
 * @param {number} x
 * @return {void}
 */
MaxStack.prototype.push = function (x) {
    this.stack.push(x);

    // check 2 scenarios; if any true, reset max
    // S1: No max value
    // S2: x is greater than max value
    if ( x >= this.maxVal || this.maxVal === null || this.maxVal === undefined){
        this.maxVal = x;
        this.maxValIndex = this.stack.length - 1;
    }
};

/**
 * @return {object}
 */
MaxStack.prototype.pop = function() {
    // check that stack is not null
    if (this.stack.length >= 1) {
        const poppedVal = this.stack.pop();
        // because you are removing from the array, you need to reset the max
        this._setNewMax();
        // after you reset, return
        return poppedVal;
    }
    return null;
};

/**
 * @return {number, null}
 */
MaxStack.prototype.top = function() {
    if (this.stack.length >= 1) {
        return this.stack[this.stack.length - 1];
    }
    return null;
};

/**
 * @return {number, null}
 */
MaxStack.prototype.peekMax = function() {
    return this.maxVal;
};

/**
 * @return {object}
 */
MaxStack.prototype.popMax = function() {
    if (this.stack.length >= 1) {
        // use splice to remove the value from the array
        const poppedMaxVal = this.stack.splice(this.maxValIndex,1);
        // reset max
        this._setNewMax();
        return poppedMaxVal;

    }
    return null;
};


// Scenario 1
const obj = new MaxStack();
console.log(`Objected Created: ${JSON.stringify(obj)}`);
obj.push(5);
console.log(`Add 5: ${JSON.stringify(obj)}`);
obj.push(1);
console.log(`Add 1: ${JSON.stringify(obj)}`);
obj.push(5);
console.log(`Add 5: ${JSON.stringify(obj)}`);
const top1 = obj.top();
console.log(`Get top num: ${top1}`);
const popMax1 = obj.popMax();
console.log(`Popped max num: ${popMax1}`);
const top2 = obj.top();
console.log(`Get top num: ${top2}`);
const peekMax1 = obj.peekMax();
console.log(`Show Max: ${peekMax1}`);
const pop1 = obj.pop();
console.log(`Pop: ${pop1}`);
const top3 = obj.top();
console.log(`Get top num: ${top3}`);


// Scenario 2
// const obj2 = new MaxStack();
// console.log(`Objected Created: ${JSON.stringify(obj2)}`);
// obj2.push(5);
// console.log(`Add 5: ${JSON.stringify(obj2)}`);
// obj2.push(1);
// console.log(`Add 1: ${JSON.stringify(obj2)}`);
// const popMax1 = obj2.popMax();
// console.log(`Popped max num: ${popMax1}`);
// const peekMax1 = obj2.peekMax();
// console.log(`Show Max: ${peekMax1}`);