#Emily Murphy
#2017-11-17
#matrixDemo.py - how to create and use matrix (list inside of list)

board = [['a','b','c'],['d','e','f'],['g','h','i']]

def printBoard():
    for row in range(0,3):
        for col in range(0,3):
            print(board[row][col], end = ' ')
        print()
        
printBoard()

row = int(input('Enter row number: '))
col = int(input('Enter column number: '))

board[row-1][col-1] = 'x'

printBoard()