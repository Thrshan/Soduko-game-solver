import numpy as np
import os

# Checks for the position i, j is valid for number x
def valid_position(board, i, j, x):
    mod_i = (((( i + 1 ) * 2 // 7 ) + 1 ) * 3 )
    mod_j = (((( j + 1 ) * 2 // 7 ) + 1 ) * 3 )
    if x in board[i, :] or x in board[:, j] or x in board[mod_i - 3: mod_i, mod_j - 3: mod_j,]:
        return False
    return True


script_dir = os.path.dirname(__file__)
ex_file = os.path.abspath(os.path.join(script_dir, '../example/puzzle1.txt'))
puzzle_file = open(ex_file, 'r')  # text file containing sudoku
log_file = open('log.txt', 'w')

# Initializing all the required variables
puzzle_list = [[]]*9
flag = True
now = 1
max_count = 500000
row, col, val = [], [], []

# Taking data from text file and converting into numpy array
for i, line in enumerate(puzzle_file):
    puzzle_list[i] = list(line.strip().split())
    
for i in range(9):
    for j in range(9):
        puzzle_list[i][j] = int(puzzle_list[i][j]) #  string to integer - for every element

puzzle = np.array(puzzle_list)
in_puzzle = np.array(puzzle_list)  # Making a copy of the starting puzzle

i, j, count = 0, 0, 0

while True:
    if j == 9:  # Once column pointer(j) hits the end of row, Reset the column and increment the row
        j, i = 0, i + 1
    #i = 0 if i == 9 else i  # Once row pointer(i) hits the end of table, Reset to 0
    
    if puzzle[i, j] == 0:
        count += 1
        for x in range(now, 10):
            if valid_position(puzzle, i, j, x):
                puzzle[i, j] = x
                row.append(i); col.append(j); val.append(x)
                break
        else:  # Tried 1-9 in the slot i, j and nothing fits, Go back and relace what you added last with next new valid number
            if len(val) == 0:
                print('This puzzle have no solution')
                break
            else:
                i = row.pop()
                j = col.pop()
                puzzle[i, j] = 0
                now = val.pop() + 1
                flag = False
    if flag:
        j += 1
        now = 1
    else: 
        flag = True
    
    if 0 not in puzzle:
        break
    elif count == max_count:
        print('Taking too many attempts, Increase the max_count to try further')
        break
    
    
print(count)
puzzle_file.close()
log_file.close()