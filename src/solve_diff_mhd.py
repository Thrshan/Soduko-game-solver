import numpy as np
import os
import time
t1=time.time()
# Checks for the position i, j is valid for number x

script_dir = os.path.dirname(__file__)
ex_file = os.path.abspath(os.path.join(script_dir, '../example/puzzle6.txt'))
puzzle_file = open(ex_file, 'r')  # text file containing sudoku

# Initializing all the required variables
puzzle = [[]]*9

# Taking data from text file and converting into numpy array
for i, line in enumerate(puzzle_file):
    puzzle[i] = list(line.strip().split())
    
for i in range(9):
    for j in range(9):
        puzzle[i][j] = int(puzzle[i][j]) #  string to integer - for every element


def possible(y, x, n):
	global puzzle
	for i in range(0,9):
		if puzzle[y][i] == n:
			return False
	for i in range(0,9):
		if puzzle[i][x] == n:
			return False
	x0 = (x // 3) * 3
	y0 = (y // 3) * 3
	for i in range(0,3):
		for j in range(0,3):
			if puzzle[y0 + i][x0 + j] == n:
				return False
	return True

def slove():
	global puzzle
	for y in range(9):
		for x in range(9):
			if puzzle[y][x] == 0:
				for n in range(1,10):
					if possible(y, x, n):
						puzzle[y][x] = n
						slove()
						puzzle[y][x] = 0
				return
	print(np.matrix(puzzle));t2=time.time();print(t2-t1)
	input("More?")

slove()