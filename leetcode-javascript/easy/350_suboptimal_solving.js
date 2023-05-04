// 350. Interesection of Two Arrays
// COME BACK TO: https://leetcode.com/problems/intersection-of-two-arrays-ii/
// SOLVED? Yes, but can be faster and have better memory usage

// Given two arrays, write a function to compute their intersection.
// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Note:
// Each element in the result should appear as many times as it shows in both arrays.
// The result can be in any order.
// Follow up:

// What if the given array is already sorted? How would you optimize your algorithm?
// What if nums1's size is small compared to nums2's size? Which algorithm is better?
// What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

// more legible; fewer tricks
const createCounter = arr => {
	let count = {};
	arr.forEach(val => count[val] = (count[val] || 0) + 1);
	return count;
}


const getIntersection = (nums1, nums2) => {
	const countNums1 = createCounter(nums1);
	const countNums2 = createCounter(nums2);
	const intersection = [];

	for (let num in countNums1) {
		if (num in countNums2) {
			let fill;
			if (countNums1[num] > countNums2[num]) {
				fill = countNums2[num];
			} else {
				fill = countNums1[num];
			}
			for( let i=0; i < fill; i++ ) {
				intersection.push(num);
			}
		}
	}
	return intersection;
};

// console.log(getIntersection([1,2,2,1],[2,2]));

// faster
const intersect = (nums1, nums2) => {
	const intersection = [];

	const mapOfnums1 = new Map();

	for (const num in nums1) {
		if (mapOfnums1.has(num)){
			mapOfnums1.set(num, mapOfnums1.get(num) + 1);
		} else {
			mapOfnums1.set(num, 1);
		}
	}

	for (const num in nums2){
		if (mapOfnums1.has(num) && mapOfnums1.get(num) > 0) {
			intersection.push(num);
			mapOfnums1.set(num, mapOfnums1.get(num) - 1);
		}
	}

	return intersection;
};

console.log(intersect([1,2,2,1],[2,2]));
// NOT WORKING, get it to work
// THEN TRY THIS APPROACH

var intersect = function(nums1, nums2) {
	obj = {};
	result = [];
	for(let i of nums1){
		obj[i] = obj[i] ? obj[i]+1 : 1
	}
	for(let i of nums2){
		if(obj[i]){
			obj[i]--
			result.push(i)
		}
	}
	return result
};

//Even Better Solution with less memory usage

var intersect = function(nums1, nums2) {
	let a1 = nums1.sort((a,b)=> a-b);
	let a2 = nums2.sort((a,b)=> a-b);
	let result = [];
	while(a1.length && a2.length){
		if(a1[0] === a2[0]){
			result.push(a1.shift());
			a2.shift();
		}
		else if(a1[0] > a2[0]){
			a2.shift();
		}else{
			a1.shift();
		}
	}
	return result
};