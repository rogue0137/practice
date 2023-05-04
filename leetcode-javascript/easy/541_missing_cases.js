// 541. Reverse String II
// COME BACK TO: link
// SOLVED? YES, BUT FOR NOT ALL CASES
// Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
// Example:
// Input: s = "abcdefg", k = 2
// Output: "bacdfeg"
// Restrictions:
// The string consists of lower English letters only.
// Length of the given string and k will in the range [1, 10000]
///
// Wrong Answer
// Input: "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39
// Output: "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
// Expected: "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"

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
    let newArray = [];
    let stringToReturn;
    

    if ( lenOfString < k) {
        newArray = stringAsArray;
        newArray.reverse();
        stringToReturn = newArray.join("");
    } else if ( k === 1 ) {
        stringToReturn = s;
    } else {
        // for every k in 2k, reverse
        for (let start = 0, middle = k; end = twoK, start < lenOfStringMinusRemainder; start += twoK, middle += twoK, end += twoK){
            const firstK = stringAsArray.slice(start,middle);
            firstK.reverse();
            const nextK = stringAsArray.slice(middle,end);
            newArray = newArray.concat(firstK);
            newArray = newArray.concat(nextK);
        }

        if (lenOfString > twoK) {
            let restOfK;
            if (isLessThanK) {
                // less than k, reverse all
                restOfK = stringAsArray.slice(lenOfStringMinusRemainder, lenOfString);
                restOfK.reverse;
                
            } else {
                // less than 2k but >= k, reverse first k char, leave other original
                firstHalfOfRestOfK = stringAsArray.slice(lenOfStringMinusRemainder, lenOfStringMinusRemainder + k);
                firstHalfOfRestOfK.reverse();
                secondHalfOfRestOfK = stringAsArray.slice(llenOfStringMinusRemainder + k, lenOfString);
                restOfK = firstHalfOfRestOfK + secondHalfOfRestOfK;
            }

            newArray = newArray.concat(restOfK);
        }

        stringToReturn = newArray.join("");

    }


    return stringToReturn
};
//console.log(reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39));
