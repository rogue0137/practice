# 616. Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        str_to_array = list(s)
        len_str = len(str_to_array)