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

console.log(getIntersection([1,2,2,1],[2,2]));