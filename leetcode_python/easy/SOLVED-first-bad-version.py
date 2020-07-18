# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        L = 1
        R = n
        
        while L < R:
            mid = (L + R) // 2
            mid_bad = isBadVersion(mid)
            if mid_bad:
                R = mid
            else:
                L = mid + 1
        return L


# Runtime: 52 ms, faster than 8.09% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.9 MB, less than 22.56% of Python3 online submissions for First Bad Version.