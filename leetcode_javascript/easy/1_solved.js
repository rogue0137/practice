// AMAZON
// 1. Two Sum
// SOLVED? YES

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:

// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

const twoSum = (nums, target) => {
	const mapOfNums = {};
	for (const index in nums){
		const secondNum = target - nums[index];
		if ( secondNum in mapOfNums) {
			return [ mapOfNums[secondNum], index ]
		} else{
			mapOfNums[nums[index]] = index;
		}
	}  
};

console.log(twoSum([2, 7, 11, 15],9));