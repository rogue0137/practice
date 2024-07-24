import random
import sys
import math

def createBoard():
    # Create a 60x15 matrix
    board = []

    # columns
    for x in range(60):
        board.append([])
        # rows
        for y in range(15):
            if random.randint(0, 1) == 0:
                # ocean
                board[x].append('~')
            else:
                # land
                board[x].append('*')

    return board


def drawBoard(board):
    tenDigitsLine = '   '
    for i in range(1, 6):
        tenDigitsLine += (' '* 9) + str(i)
    print(tenDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print(f'{extraSpace}{row} {boardRow} {row}')
    
    print()
    print('   ' + ('0123456789' * 6))
    print(tenDigitsLine)

theBoard = createBoard()
drawBoard(theBoard)
