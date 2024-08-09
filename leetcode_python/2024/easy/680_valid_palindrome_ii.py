# https://leetcode.com/problems/valid-palindrome-ii/description/

# This is basically: take your solution for valid_palindrome (or use the wonderfulness)
# that is Python reverse string!!) and add a wrapper function on it
# to check if deleting one char in the string will get your a palindrome in the
# substring

class Solution:
    def checkPalindrome(self, sub_s: str) -> bool:
        # Yassss, reverse string to check for palindromes. 
        return sub_s == sub_s[::-1]

    def validPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            # If characters match, move towards center
            if s[left_index] == s[right_index]:
                left_index += 1
                right_index -= 1
            else:
                # Check if removing either character results in a palindrome:
                # This is VERY verbose, but I'm using many variable names so it is
                # super obvious what we're checking at all times.
                # Also, this is your Slice Notation Reminder: s[inclusive:exclusive]
                canRemoveRightChar = self.checkPalindrome(s[left_index:right_index])
                canRemoveLeftChar = self.checkPalindrome(s[left_index + 1:right_index + 1])
                canRemoveOneChar = (canRemoveRightChar == True) or (canRemoveLeftChar == True) 
                return canRemoveOneChar
        

        # If no mismatches found, s is already a palindrome
        return True







        