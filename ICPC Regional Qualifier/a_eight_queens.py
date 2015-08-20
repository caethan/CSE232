import sys
import numpy as np

#Read in the board
board = np.empty((8,8), dtype=bool)
for i in range(8):
    line = sys.stdin.readline().strip()
    row = np.array([char for char in line])
    board[i,:] = row == '*'
    
#Check for row and column collisions
if not (board.sum(axis=0) == 1).all():
    print 'invalid'
    
elif not (board.sum(axis=1) == 1).all():
    print 'invalid'
    
#Check for diagonal collisions
else:
    status = 'valid'
    for i in range(8):
        queencol = np.arange(8)[board[i,:]]
        for j in range(i+1,8):
            thiscol = np.arange(8)[board[j,:]]
            if abs(queencol - thiscol) == abs(i - j):
                status = 'invalid'
                break
    print status
        