const assert = require("assert");

// Approach #1 Single Scan [Accepted]
// const canPlaceFlowers = (flowerbed, n) => {
//     let flowersAdded = 0;
//     let index = 0;
//
//     while (index < flowerbed.length) {
//         // 3 things must be true to add a flower
//         // 1. flower bed at index must be 0
//         // 2. i should be 0 OR i minus 1 index should be 0
//         // 3. i equals len of flowerbed minus 1 OR i plus 1 index should be 0
//         if (
//             (flowerbed[index] === 0) &&
//             (index === 0 || flowerbed[ index - 1] === 0) &&
//             (index === flowerbed.length - 1 || flowerbed[index + 1] === 0)
//         )
//         {
//             flowerbed[index] = 1; // updates the array
//             flowersAdded++;
//         }
//         index++;
//     }
//
//     return flowersAdded >= n;
// };


// Approach #2 Optimized [Accepted]
// same as above with one exception:
// you check n at every loop and break if it matches
const canPlaceFlowers = (flowerbed, n) => {
    let flowersAdded = 0;
    let index = 0;

    while (index < flowerbed.length) {
        // 3 things must be true to add a flower
        // 1. flower bed at index must be 0
        // 2. i should be 0 OR i minus 1 index should be 0
        // 3. i equals len of flowerbed minus 1 OR i plus 1 index should be 0
        if (
            (flowerbed[index] === 0) &&
            (index === 0 || flowerbed[ index - 1] === 0) &&
            (index === flowerbed.length - 1 || flowerbed[index + 1] === 0)
        )
        {
            flowerbed[index] = 1; // updates the array
            flowersAdded++;
        }
        if (flowersAdded === n || n === 0) {
            return true;
        }
        index++;
    }

    return false;
};

assert(canPlaceFlowers([1,0,0,0,1],1), true);
assert(canPlaceFlowers([1,0,0,0,0,0,1],2), true);
assert(canPlaceFlowers([0,0,0,0,0,1,0,0],
0), true);