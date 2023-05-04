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
