1313. Decompress Run-Length Encoded List
https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        len_of_nums = len(nums)
        new_array = []
        for i in range(0, len_of_nums, 2):
            freq = nums[i]
            val = nums[i + 1]
            generated_array = [val] * freq
            new_array = new_array + generated_array
        return new_array

Runtime: 68 ms, faster than 73.81% of Python3 online submissions for Decompress Run-Length Encoded List.
Memory Usage: 14 MB, less than 76.20% of Python3 online submissions for Decompress Run-Length Encoded List.