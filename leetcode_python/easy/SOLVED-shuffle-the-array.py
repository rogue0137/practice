1470. Shuffle the Array
URL: https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        shuffle_nums = []
        for i in range(0,n):
            shuffle_nums.append(first_half[i])
            shuffle_nums.append(second_half[i])
        return shuffle_nums

# Runtime: 92 ms, faster than 35.30% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.