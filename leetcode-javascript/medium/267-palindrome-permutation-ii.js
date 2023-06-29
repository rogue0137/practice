/**
 * Some notes:
 *  - Generating all permutations of a string is inherently an O(n!) operation,
 *    as there are n! possible permutations for a string of length n
 *  - The below gets rid of duplicates by using a Set() to store the permutations
 *  - It is possible to only create non-duplicate permutations in the first place
 *  - However, that approach's worst case is still O(n!)
 */
/**
 * @param {string} s
 * @return {string[]}
 */
const generatePalindromes = function(s) {
    // 1. Break up the string
    const splitString = s.split('');
    
    // 2. Create a map of key: letter, value: # of letter in string
    const letterMap = new Map();
    for (let letter of splitString) {
        if (letterMap.has(letter)) {
            letterMap.set(letter, letterMap.get(letter) + 1);
        } else {
            letterMap.set(letter, 1);
        }
    }

    // 3. Create the halfString
    let halfString = '';

    // 4. Account for oddLetterValues
    let oddLetter;
    let lettersWithOdd = 0;

    // 5. Build the halfString and find any oddLetterValues
    for (let [letter, count] of letterMap.entries()) {
        // Check for letters with an odd # of that letter in the original string
        if (count % 2 !== 0) {
            lettersWithOdd += 1;
            // If there are more than two letters with odd values,
            // you cannot make valid palindromes from the string
            // so return an empty array
            // Checking here helps us break out of the function early
            if (lettersWithOdd == 2 ) {
                return [];
            }
            oddLetter = letter;
        } 
        // You want to divide by two for all numbers of letters
        // However, you need to round down to account for an odd # of letters
        // if you have a letter with an odd # of itself in the string
        halfString += letter.repeat(Math.floor(count / 2));
    }

    // 7. Use the permutations function to create all possible permutations of the halfString
    const halfPermutations = getPermutations(halfString);
    // Because getPermutations returns a Set, we do not need a Set for palindromicPermutations
    // since we will have already filtered out duplicates
    const palindromicPermutations = [];

    // 8. If oddLetter is defined, add the oddLetter to the middle of each permutation
    // else add the reverse of the permutation to the end of the permutation
    if (oddLetter !== undefined) {
        for (let permutation of halfPermutations) {
            palindromicPermutations.push(permutation + oddLetter + permutation.split('').reverse().join(''));
        }  
    } else {
        for (let permutation of halfPermutations) {
            palindromicPermutations.push(permutation + permutation.split('').reverse().join(''));
        }  
    }

    // 9. Return the palindromicPermutations as an array
    const arrayOfPalindromicPermutations = Array.from(palindromicPermutations);

    return arrayOfPalindromicPermutations;
};

// 6. Function to actually create palindromicPermutations
// Below we are using Set() to avoid duplicates
// Remember that string below will be the halfString
const getPermutations = function(string, prefix = '') {
    if (string.length <= 1 ) {
        return new Set([prefix + string]);
    } else {
        let permutations = new Set();
        // Iterate through all of the halfString letters
        for (let i = 0; i < string.length; i++) {
            // Separate a specific char from the rest of the string
            let char = string[i];
            let remainingString = string.slice(0, i) + string.slice(i+1);
            // This will recursively call the function until the string is empty
            // We'll keep adding a char to the prefix until the remainingString is empty
            for (let perm of getPermutations(remainingString, prefix + char)) {
                permutations.add(perm);
            }
        }
        return permutations;
    } 
}

