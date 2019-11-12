//find the nth number in the fib sequence
// const { describe, it } = require('mocha');
// const assert = require('assert');

const getFibNthNumber = nth => {

    let fibonnaciNumbers = [0, 1];

    //if nth > 2, we need to generate more fibonacci numbers
    if (nth > 2) {
        for (let i = 0; i < nth; i++) {
            const numberOfFibsGenerated = fibonnaciNumbers.length;
            const lastFib = fibonnaciNumbers[numberOfFibsGenerated - 1];
            const previousToLastFib = fibonnaciNumbers[numberOfFibsGenerated - 2];

            //create  new fib from the previous 2
            const newFibNumber = lastFib + previousToLastFib;
            //push the newly created fib to the array of fibs
            fibonnaciNumbers.push(newFibNumber);

        }
    }
    const nThFibonacciNumber = fibonnaciNumbers[nth - 1];
    return nThFibonacciNumber;
}

//TESTS
console.log(`${getFibNthNumber(1)} should be 0`);
console.log(`${getFibNthNumber(2)} should be 1`);
console.log(`${getFibNthNumber(3)} should be 1`);
console.log(`${getFibNthNumber(4)} should be 2`);
console.log(`${getFibNthNumber(5)} should be 3`);
console.log(`${getFibNthNumber(6)} should be 5`);
console.log(`${getFibNthNumber(7)} should be 8`);