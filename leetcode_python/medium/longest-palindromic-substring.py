# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        len_s = len(s)
        for i in range(len_s):
            print(f'i: {i}')
            palindrome1 = self.find_palindrome(s, i, i)
            palindrome2 = self.find_palindrome(s, i, i+1)
            print(f'longest_palindrome: {longest_palindrome}\npalindrome1: {palindrome1}\npalindrome2:{palindrome2}')
            longest_palindrome = max([longest_palindrome, palindrome1, palindrome2], key=lambda x: len(x))
        return longest_palindrome
    def find_palindrome(self, s: str, left_index:int, right_index:int) -> str:
        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            left_index -= 1
            right_index += 1
        palindrome = s[left_index + 1:right_index]
        return palindrome

# Runtime: 1028 ms, faster than 66.42% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 62.08% of Python3 online submissions for Longest Palindromic Substring.