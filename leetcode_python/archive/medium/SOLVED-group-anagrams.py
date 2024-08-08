# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_as_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if output_as_dict.get(sorted_s):
                output_as_dict[sorted_s].append(s)
            else:
                output_as_dict[sorted_s] = [s]
        output_as_array = []
        for k, v in output_as_dict.items():
            output_as_array.append(v)
        return output_as_array

# Runtime: 96 ms, faster than 90.74% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.4 MB, less than 97.68% of Python3 online submissions for Group Anagrams.