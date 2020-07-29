# https://leetcode.com/problems/edit-distance/
# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # get len
        n = len(word1)
        m = len(word2)
        
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # create grid
        # how many columns = [0] * (m + 1)
        # how many rows with the above columns = for _ in range(n + 1)
        d = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # fill in first col (2nd number doesn't change; always 0)
        for i in range(n + 1):
            d[i][0] = i
        
        # fill in first row (1st number doesn't change, always 0)
        for j in range(m + 1):
            d[0][j] = j
        

        # DP compute 
        # fill in the rest starting at (1, 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + 1
                above = d[i][j - 1] + 1
                horizontal = d[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    horizontal += 1
                d[i][j] = min(left, above, horizontal)
        
        return d[n][m]