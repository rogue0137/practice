// 387. First Unique Character in a String
// COME BACK TO: https://leetcode.com/problems/first-unique-character-in-a-string/
// SOLVED? YES, BUT VERY INEFFICENTLY
// Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.
// Note: You may assume the string contain only lowercase letters.

const createCounter = arr => {
  let count = {};
  arr.forEach(val => count[val] = (count[val] || 0) + 1);
  return count;
}
const firstUniqChar = s => {
    const arrayFromString = Array.from(s);
    const counter = createCounter(arrayFromString);
    const lessThanOne = [];
    for (let c in counter) {
        if (counter[c] === 1){
            lessThanOne.push(c);
        }
    }
   for (const [index, char] of arrayFromString.entries()){
        if (lessThanOne.includes(char)) {
            return index;
        }
    }

    return -1;
};

console.log(firstUniqChar("loveleetcode"));