# https://leetcode.com/problems/edit-distance/
# 72. Edit Distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # horse, ros grid
        #   _ R O S
        # _ 0 1 2 3 
        # H 1 1 2 3
        # O 2 2 1 2
        # R 3 2 2 3
        # S 4 3 3 2
        # E 5 4 4 3
        # Ex. HOR and RO
        # above: HO and RO, edit distance between these
        # diagonal: HO and R edit distance between these
        # left: HOR and R edit distance between these
        # answer = 3
        
        # create grid
        len_word1 = len(word1)
        len_word2 = len(word2)
        grid = []
        
        # if time, do list comprehension
        for i in range(len_word1 + 1): # 3 + 1 = 4
            grid.append([])
            for j in range(len_word2 + 1): # 5 + 1 = 6
                grid[i].append(0)
        
        # set first column
        for i in range(len_word1 + 1):
            grid[i][0] = i
        # set first row
        for j in range(len_word2 + 1):
            grid[0][j] = j
            
        # set the rest of grid based on possibilities
        for i in range(1, len_word1 + 1):
            char1 = word1[i - 1]
            for j in range(1, len_word2 + 1):
                char2 = word2[j - 1]
                
                # look above
                above = grid[i - 1][j]
                
                # look diagonal 
                diagonal = grid[i - 1][j - 1]
                # if same char, one less edit distance
                if char1 == char2:
                    diagonal -= 1

                # look left
                left = grid[i][j - 1]
                min_of_three = min(above, diagonal, left)
                grid[i][j] = min_of_three + 1
                
        # take the last output of the grid
        last_square = grid[len_word1][len_word2]
        return last_square
# Runtime: 208 ms, faster than 44.06% of Python3 online submissions for Edit Distance.
# Memory Usage: 17.4 MB, less than 48.55% of Python3 online submissions for Edit Distance.


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