// https://leetcode.com/problems/unique-number-of-occurrences/submissions/


/**
 * Basic solution
 * 
 * Runtime: 59 ms, Beats 33.13%of users with JavaScript
 * Memory: 42.61 mb, Beats 54.99%of users with JavaScript
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    // create a hashmap of integers
    const mapFromIntegers = new Map();

    // check if value is already in the hashmap
    for (let i of arr){
    // if in the hashmap, increment value
        if (mapFromIntegers.get(i)){
            const value = mapFromIntegers.get(i);
            mapFromIntegers.set(i, value + 1)
    // if not in the hashmap, add to hashmap and set value to 1
        } else {
            mapFromIntegers.set(i, 1);
        }
    }

    // console.log(mapFromIntegers);
    // get sorted list of values only
    const arrayOfOnlyValuesFromMap = Array.from(mapFromIntegers.values()).sort();

    // if any number is seen more than once, return false
    // console.log(arrayOfOnlyValuesFromMap);
    for (let i=1; i < arrayOfOnlyValuesFromMap.length; i++) {
        const currentValue = arrayOfOnlyValuesFromMap[i];
        const previousValue = arrayOfOnlyValuesFromMap[i - 1];
        if (currentValue === previousValue) {
            return false
        }
    }
    
    return true;
};


/**
 * More performant solution using a set:
 * 
 * Runtime: 47 ms, Beats 88.73%of users with JavaScript
 * Memory: 42.51MB, Beats 62.30%of users with JavaScript
 * 
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    // create a hashmap of integers
    const mapFromIntegers = new Map();

    // check if value is already in the hashmap
    for (let i of arr){
    // if in the hashmap, increment value
        if (mapFromIntegers.get(i)){
            const value = mapFromIntegers.get(i);
            mapFromIntegers.set(i, value + 1)
    // if not in the hashmap, add to hashmap and set value to 1
        } else {
            mapFromIntegers.set(i, 1);
        }
    }

    // create a set of the values
    const setOfValues = new Set(Array.from(mapFromIntegers.values()));

    const sizeOfMap = mapFromIntegers.size;
    const sizeOfSet = setOfValues.size;
    // console.log(sizeOfMap, sizeOfSet);

    //if the size of the map and the size of the set are the same, every integer has a unique number of occurrences
    if (sizeOfMap === sizeOfSet ){
        return true;
    }
    
    return false;
};
