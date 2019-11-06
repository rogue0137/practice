// AMAZON

// 937. Reorder Data in Log Files
// COME BACK TO: Yes
// SOLVED? Yes


// You have an array of logs.  Each log is a space delimited string of words.

// For each log, the first word in each log is an alphanumeric identifier.  Then, either:

// Each word after the identifier will consist only of lowercase letters, or;
// Each word after the identifier will consist only of digits.
// We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

// Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

// Return the final order of the logs.

 

// Example 1:

// Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
// Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

// Constraints:

// 0 <= logs.length <= 100
// 3 <= logs[i].length <= 100
// logs[i] is guaranteed to have an identifier, and a word after the identifier.
// Accepted

const reorderLogFiles = logs => {
	const letterRegex = /[a-z]/i;
	// IS IT BETTER TO USE A FOR LOOP OR USE A FILTER 
	// TO SHOW YOU KNOW HOW TO USE IT?
	// Code is 52 ms faster than 98.82% submission with for loop
	// Code is faster than 5% of submissions with two filters
	// const letterLogs = logs.filter( log => {
	// 	const splitLog = log.split(" ");
	// 	return splitLog[1].match(letterRegex)
	// });
	// const digitLogs = logs.filter(log => {
	// 	const splitLog = log.split(" ");
	// 	return !splitLog[1].match(letterRegex)
	// });

	const letterLogs = [];
	const digitLogs = [];
	for (const i in logs){
		console.log(`log: ${logs[i]}`);
		const splitLog = logs[i].split(" ");
		console.log(`splitlog: ${splitLog}`);
		const isLetter = splitLog[1].match(letterRegex);
		if (isLetter) {
			letterLogs.push(logs[i]);
		} else {
			digitLogs.push(logs[i]);
		}
	}

	const logSection = ls => ls.slice(ls.indexOf(" ") + 1);

	const compare = (ls1, ls2) => {
		console.log(`ls1: ${ls1}, ls2: ${ls2}`);
		// what is a better name for n? 
    	const n = logSection(ls1).localeCompare(logSection(ls2));
    	console.log(`N: ${n}`);

    	if (n !== 0) {
    		return n;
    	} else {
    		return ls1.localeCompare(ls2);
    	}
    	
  	};

	const reorderedLog = [...letterLogs.sort(compare), ...digitLogs];
	return reorderedLog;
};

const logs = ["dig1 8 1 5 1","let1 art can","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"];
console.log(reorderLogFiles(logs));

// LEARNINGS
// String.prototype.localeCompare() method returns a number indicating 
// whether a reference string comes before or after or is the same as 
// the given string in sort order