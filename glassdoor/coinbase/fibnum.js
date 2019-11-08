//find the nth number in the fib sequence
// const { describe, it } = require('mocha');
// const assert = require('assert');

const getFibNthNumber = nth => {
    let f; // first
    let n; // second
    let num;
    for (let i = 0; i < nth + 1; i++){
        console.log(`i: ${i}`);
        if (i === 0 ) {
            f = 0;
            num = 0;
        } else if ( i === 1 ){
            n = 1;
            num = 1;
        } else {
            num = f + n;
            f = n;
            n = num;
        }
        console.log(`num: ${num}`);
    }

    return num;
}

// describe('Fib Nth number', function() {
//     it('should return 1 when Nth position is 2 index', function() {
//        assert.equal(getFibNthNumber(2), 1);
//     });
//     it('should return 13 when Nth position is 6 index', function() {
//         assert.equal(getFibNthNumber(6),13);
//     });
//     it('should return 144 when Nth position is 12 index', function() {
//         assert.equal(getFibNthNumber(12), 144);
//     });
// });

console.log(getFibNthNumber(6));