// PROMPT 1:
// Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
// Example:
// Input: s = "abcdefg", k = 2
// Output: "bacdfeg"
// Restrictions:
// The string consists of lower English letters only.
// Length of the given string and k will in the range [1, 10000]
///

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */

const lessThanK = (num, k) => {
    if (num < k){
        return true;
    } else {
        return false;
    }     
}

const reverseStr = (s, k) => {
    const lenOfString = s.length; 
    const stringDividedByK = lenOfString/k;
    const remainder = lenOfString % k;
    const isLessThanK = lessThanK(remainder, k); 
    const lenOfStringMinusRemainder = lenOfString - remainder;
    const twoK = 2 * k;
    const stringAsArray = Array.from(s);
    const newArray = [];
    
    
    // console.log(`len of string: ${lenOfString} \n len of k: ${k}`);
    // console.log(`2k is ${twoK}`);
    // console.log(`K goes into string fully ${stringDividedByK} times`);
    // console.log(`Remainder is ${remainder}`);
    // console.log(`The remainder is less than k: ${isLessThanK}`);
    // console.log(`This is the string as an array: ${stringAsArray}`);
    // console.log(`The len of string minus remainder is: ${lenOfStringMinusRemainder}`);

    console.log(`string as arary: ${stringAsArray}`);
    // for every k in 2k, reverse
    for (let start = 0, middle = k; end = twoK, start < lenOfStringMinusRemainder; start += twoK, middle += twoK, end += twoK){
    	const firstK = stringAsArray.slice(start,middle);
	    console.log(`firstK: ${firstK}`);
	    firstK.reverse();
	    console.log(`firstK reversed: ${firstK}`);
	    const nextK = stringAsArray.slice(middle,end);
	    console.log(`nextK: ${nextK}`);
	    newArray.push(firstK);
	    newArray.push(nextK);
	    console.log(`newArray: ${newArray}`);
    }
  
  	let restOfK;

    if (isLessThanK) {
        // less than k, reverse all
        restOfK = stringAsArray.slice(lenOfStringMinusRemainder, lenOfString);
        console.log(`restOfK: ${restOfK}`);
        restOfK.reverse;
        
    } else {
        // less than 2k but >= k, reverse first k char, leave other original
        firstHalfOfRestOfK = stringAsArray.slice(lenOfStringMinusRemainder, lenOfStringMinusRemainder + k);
        firstHalfOfRestOfK.reverse();
        secondHalfOfRestOfK = stringAsArray.slice(llenOfStringMinusRemainder + k, lenOfString);
        restOfK = firstHalfOfRestOfK + secondHalfOfRestOfK;
        console.log(`restOfK: ${restOfK}`);
    }

    console.log(`length of newArray #1: ${newArray.length}`);
    newArray.push(restOfK);
   	console.log(`length of newArray #2: ${newArray.length}`);   
   	console.log(' ')
   	console.log(newArray[0]);
   	console.log(newArray[1]);
   	console.log(newArray[2]);
   	console.log(newArray[3]);
   	console.log(newArray[4]);
   	console.log(' ')





    console.log(`full newArray: ${newArray}`);
    console.log(`length of newArray: ${newArray.length}`);
    console.log(`new array is array: ${Array.isArray(newArray)}`);
    const stringToReturn = `[${newArray}]`;
    console.log(`string to return: ${stringToReturn}`);
      
    return stringToReturn
};

reverseStr("abcdefg",2);