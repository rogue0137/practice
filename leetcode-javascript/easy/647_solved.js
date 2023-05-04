// 647. Longest Continuous Increasing Subsequence
// COME BACK TO: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
// SOLVED? Not yet tried 
// Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

// Example 1:
// Input: [1,3,5,4,7]
// Output: 3
// Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
// Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
// Example 2:
// Input: [2,2,2,2,2]
// Output: 1
// Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
// Note: Length of the array will not exceed 10,000.
const findLengthOfLCIS = nums => {
    let maxIncSeq = 1;
    if (!Array.isArray(nums) || !nums.length) {
        maxIncSeq = 0;
    } else {
        let prevNum;

        let countInSeq = 1;
        for (let i in nums) {
            if (i == 0 ) {
                prevNum = nums[i];
            } else {
                if ( nums[i] > prevNum) {
                    countInSeq += 1;
                    maxIncSeq = Math.max(maxIncSeq, countInSeq);
                } else {
                    countInSeq = 1;
                }
                prevNum = nums[i];
            }
        }
    }
    return maxIncSeq;
};

console.log(findLengthOfLCIS([1,3,5,4,7]));