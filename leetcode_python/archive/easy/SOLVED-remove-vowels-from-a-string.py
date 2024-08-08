# 1119. Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        new_list = []
        str_to_list = list(S)
        for char in str_to_list:
            if char in vowels:
                continue
            new_list.append(char)
        if len(new_list) != 0:
            new_string = ''.join(new_list)
        else:
            new_string = ''
        
        return new_string

# Runtime: 28 ms, faster than 70.89% of Python3 online submissions for Remove Vowels from a String.
# Memory Usage: 13.8 MB, less than 72.89% of Python3 online submissions for Remove Vowels from a String.