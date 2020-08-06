# 999. Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/

# 8 x 8 board
# '.' = empty
# white rook = 'R'
# white bishops = 'B'
# black pawns = 'p'
# uppercase = whie pieces
# lowercase = black pieces

# true question: of the avaiable pawns on the board, which are actually accessible and able to be captured by the rook

# FIND ROOK FIRST APPROACH
class Solution:
    def find_rook(self, board):
        R = []

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    # print(board[i][j])
                    # print(f'i: {i}')
                    # print(f'j: {j}')
                    R.append(i)
                    R.append(j)
                    return R
    
    def is_pawn(self, board_space):
        if board_space.islower():
            if board_space == 'p':
                return True

        return False

    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find the rook
        R = self.find_rook(board)
        row = R[0]
        col = R[1]
        
        # determine how many pawns the rook can capture
        capturable_pawns = 0

        # go up until you hit something
        up = row
        while up > 0:
            up -= 1
            board_space = board[up][col]
            if board_space != '.':
                if self.is_pawn(board_space):
                    capturable_pawns += 1
                break
        #print(f'capturable_pawns: {capturable_pawns}')
        # go down until you hit something
        down = row
        while down < 7:
            down += 1
            board_space = board[down][col]
            if board_space != '.':
                if self.is_pawn(board_space):
                    capturable_pawns += 1
                break
        #print(f'capturable_pawns: {capturable_pawns}')
        # go right until you hit something
        right = col
        while right > 0:
            right -= 1
            board_space = board[row][right]
            if board_space != '.':
                if self.is_pawn(board_space):
                    capturable_pawns += 1
                break
        #print(f'capturable_pawns: {capturable_pawns}')
        # go left until you hit something
        left = col
        while left < 7:
            left += 1
            board_space = board[row][left]
            if board_space != '.':
                if self.is_pawn(board_space):
                    capturable_pawns += 1
                break

        #print(f'capturable_pawns: {capturable_pawns}')
        return capturable_pawns

# Runtime: 32 ms, faster than 72.70% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 13.9 MB, less than 30.43% of Python3 online submissions for Available Captures for Rook.


# USE STRINGS APPROACH
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        board_len = len(board)
        row_len = len(board[0])
        
        # string conversion
        array_of_strings = []
        
        # if time permits, see if rows and columns can be done at the same time
        # rows
        for i in range(board_len):
            new_string = ''.join(board[i])
            remove_dots = new_string.replace('.','')
            array_of_strings.append(remove_dots)
            
        # columns   
        for i in range(row_len):
            new_array = []
            for j in range(board_len):
                new_array.append(board[j][i])
                if j == board_len - 1:
                    new_string = ''.join(new_array)
                    remove_dots = new_string.replace('.','')
                    array_of_strings.append(remove_dots)
        
        
        capturable_pawns = 0
        # loop through array of strings
        for string in array_of_strings:
            # if pR or Rp found, increment 
            if 'pR' in string: 
                capturable_pawns += 1
            if 'Rp' in string:
                capturable_pawns += 1
        
        return capturable_pawns
# Runtime: 32 ms, faster than 72.70% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 14 MB, less than 13.04% of Python3 online submissions for Available Captures for Rook.