// 125. Valid Palindrome
// COME BACK TO: https://leetcode.com/problems/valid-palindrome/
// SOLVED? Yes, but suboptimal speed and subtoptimal memory usage

// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
// Note: For the purpose of this problem, we define empty string as valid palindrome.
// Example 1:
// Input: "A man, a plan, a canal: Panama"
// Output: true
// Example 2:
// Input: "race a car"
// Output: false

const isAlphaNumeric = char => {
	const alphaNumeric = /[0-9a-zA-Z]/;
	if (char.match(alphaNumeric)){
		return true;
	}
	return false;
}

const isPalindrome = s => {
	const lowerCasedString = s.toLowerCase();
	const arrayFromString = Array.from(lowerCasedString);
	const alphanumericArray = arrayFromString.filter(char => isAlphaNumeric(char));
	const newString = alphanumericArray.join(""); 
	alphanumericArray.reverse(); 
	const reversedString = alphanumericArray.join("");

	console.log(`new string: ${newString} \n reversedString: ${reversedString}`);
	if (newString === reversedString){
		return true;
	}
	return false;
};


console.log(isPalindrome("race a car"));


// Another option

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // strip the string of punctuation and spaces
    const stringNoSpaces = s.replace(" ", "");
    const stringNoPunc = stringNoSpaces.replace(/[^a-z0-9]/gi, "");
    // lowercase all
    const stringLower = stringNoPunc.toLowerCase();
    // split into array
    const arrayOfAlphaNumericChar = stringLower.split("");

    // can I pop from both ends
    while (arrayOfAlphaNumericChar.length > 1 ){
        const frontArray = arrayOfAlphaNumericChar.shift()
        const backArray = arrayOfAlphaNumericChar.pop();
        if (frontArray !== backArray ) {
            return false
        }
    }

    return true;
    
};