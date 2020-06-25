# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        len_s = len(s)
        for i in range(len_s):
            # print(f'longest_palindrome: {longest_palindrome}')
            # print(f'i: {i}')
            # print('pal 1')
            palindrome1 = self.find_palindrome(s, i, i)
            # print(f'palindrome1: {palindrome1}')
            # print('pal 2')
            palindrome2 = self.find_palindrome(s, i, i+1)
            # print(f'palindrome2:{palindrome2}')
            # longest_palindrome = max([longest_palindrome, palindrome1, palindrome2], key=lambda x: len(x))
            # print(f'updating longest palindrome: {longest_palindrome}')
        return longest_palindrome
    def find_palindrome(self, s: str, left_index:int, right_index:int) -> str:
        while left_index >= 0 and right_index < len(s) and s[left_index] == s[right_index]:
            # makes sure left index is not out of bounds
            # print(f'left index greater than or equal to 0')
            # makes sure right index is not out of bounds
            # print(f'AND right index less than len of s')
            # ensures that whatever is at the indexes still match
            # print(f'AND s at both left index and right index is the same')
            # print(f's: {s}')
            # print(f'left index: {left_index}')
            # print(f'right index: {right_index}')
            # print(f's[left_index]: {s[left_index]}')
            # print(f's[right_index]: {s[right_index]}')
            # decrease left and increase right to see if the palindrome is longer than the last check
            left_index -= 1
            right_index += 1
        print('Exited while loop')
        # left index has 1 added because the last loop decremented left index and then it exited, which means the last palindrome char is 1 plus the current left_index
        # the palindrome is up to right_index, because it should not be inclusive of right_index; right index had +1 added and then exited the loop, which means the last palindrome char is at right index minus 1
        palindrome = s[left_index + 1:right_index]
        return palindrome

# Runtime: 1028 ms, faster than 66.42% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 62.08% of Python3 online submissions for Longest Palindromic Substring.