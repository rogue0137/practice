# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_s = list(s)
        palindrome_list = []
        palindrome = []
        for char in list_s:
            
            str_palindrome = " ".join(palindrome)
            palindrome_list.append(str_palindrome)
        