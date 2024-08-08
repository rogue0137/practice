# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	# Remember:
    	# strings have a len method
    	# strings are also iterable
    	# .isalnum() to test if it is alphanumeric
    	# .lower)() to compare char with the same capitalization if letters
        L, R = 0, len(s) - 1

        while L < R:
        	# this could be a while loop, but I think if looks cleaner
            if not s[L].isalnum():
                L += 1
                continue
            # this could be a while loop, but I think if looks cleaner
            if not s[R].isalnum():
                R -= 1
                continue
            # could .lower() the string at the top, but then would have to use a
            # new variable as .lower() does not change the string in place
            if L < R and s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        return True

# Runtime: 52 ms, faster than 64.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.3 MB, less than 61.83% of Python3 online submissions for Valid Palindrome.