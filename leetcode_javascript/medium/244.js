/**
 * @param {string[]} words
 */
const WordDistance = function(words) {
    this.words = words;
    this.wordsLength = words.length;
};

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
WordDistance.prototype.shortest = function(word1, word2) {
    const wordIndexOne = this.words.indexOf(word1);
    const wordIndexTwo = this.words.indexOf(word2);
    //console.log(`word1: ${wordIndexOne}, word2: ${wordIndexTwo}`);
    // need to check order of indexes and then do below
    const distanceBetweenWordsOne = wordIndexTwo - wordIndexOne;
    const distanceBetweenWordsTwo = wordIndexOne - wordIndexTwo;
    const minDistanceBetweenWords = Math.min(distanceBetweenWordsOne, distanceBetweenWordsTwo);

    return minDistanceBetweenWords;
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * var obj = new WordDistance(words)
 * var param_1 = obj.shortest(word1,word2)
 */


// TEST 1
// ["WordDistance","shortest","shortest"]
// [[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]
const obj = new WordDistance(["practice","makes","perfect","coding","makes"]);
console.log(obj);
console.log(obj.shortest("coding","practice")); // 3
console.log(obj.shortest("makes","coding")); // 1

// Test 2
// ["WordDistance","shortest","shortest"]
// [[["a","b"]],["a","b"],["b","a"]]
// const obj = new WordDistance(["a","b"]);
// console.log(obj);
// console.log(obj.shortest("a","b")); // 1
// console.log(obj.shortest("b","a")); // 1