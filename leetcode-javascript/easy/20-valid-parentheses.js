/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // string only contains these characters: '(', ')', '{', '}', '[', ']'
    // valid strings
    //  - open brackets must be closed by the same type of brackets, e.g. '(' closed by ')'
    //  - open brackets must be closed in the correct order, e.g. '({})'
    //  - every close bracket has a corresponding open bracket of the same time, e.g. ')' has corresponding '('

    const splitString = s.split('');
    if (splitString.length % 2 !== 0) {
        return false;
    }

    const closedBrackets = [')', '}', ']'];
    const bracketPairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    };

    const poppedBrackets = [];
    // console.log('poppedBrackets: ', poppedBrackets);

    
    while (splitString.length > 0) {
        const poppedFromString = splitString.pop(); // 2. ) 1. )
        // if first popped is a closedBracket, pop the next bracket(s) until you get an open bracket 
        if (closedBrackets.includes(poppedFromString)) {
            // console.log('inside closedBrackets.includes');
            // console.log('splitString.pop(): ', poppedFromString);
            poppedBrackets.push(poppedFromString); // 2. [ ']1. [ ')' ]
            // console.log('poppedBrackets: ', poppedBrackets);
            continue;
        } else {
            // console.log('poppedBrackets: ', poppedBrackets);
            // console.log('poppedFromString: ', poppedFromString);
            // if it's not another closed bracket, pop from poppedBrackets and see if poppedFromString is an open match for what you've popped from poppedBrackets
            const previouslyPoppedBrackets = poppedBrackets.pop(); 
            // console.log('previouslyPoppedBrackets: ', previouslyPoppedBrackets);
            if (previouslyPoppedBrackets === bracketPairs[poppedFromString]) { 
                continue;
            } else {
                return false;
            }
        }    
    }

    if (poppedBrackets.length === 0) {
        return true;
    } 
    
    return false;

};
