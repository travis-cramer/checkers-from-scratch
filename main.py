# Checkers
# a script to create a functioning checkers board in Terminal/Command Line
import os

bad_move_error_message = 'Invalid move, try again.'

# First, we need to define some functions to create an 8 by 8 checkered board.
alpha = 'abcdefgh'
num_lab = '12345678'

def make_board():
	board = []
	# Make empty board of right size.
	for i in range(9):
		board.append(['|||']*9)

	# Make it checkered
	for i in range(1,9,2):
		for j in range(0,9,2):
			board[i][j] = '| |'

	for i in range(2,9,2):
		for j in range(1,9,2):
			board[i][j] = '| |'

	for i in range(1, 8, 2):
		board[0][i] = '| |'
		
	# Label coordinates (A-H)
	col_lab = []
	for i in range(8):
		col_lab.append('0')
	for i in range(8):
		col_lab[i] = ' ' + alpha[i] + ' '
	for i in range(8):
		board[8][i + 1] = col_lab[i]

	# Label coordinates (1-8)
	for i in range(8):
		board[i][0] = ' ' + str(8 - i) + ' '

	# Make bottom left corner blank
	board[8][0] = '   '

	return board

def print_board(board):
	print score
	for row in board:
		print ' '.join(row)




# we will need a function that translates from checkers index (letters and numbers) to a list of lists index (a list of length 2)
def translate(command):
	# calculate old position's index from first two characters of command
	return [7 - num_lab.index(command[1]), alpha.index(command[0]) + 1]
	


# Now, we need to created the Piece class

class Piece(object):
	"""Creates a standard checkers piece"""
	def __init__(self, team, alive = True):
		self.team = team
		self.alive = alive

	def set_position(self, position):
		self.position = position

	def kill(self):
		self.alive = False

# create function for moving pieces
def move_piece(piece, new_position):
	# get old position so that we can later "fill in" board with the correct empty space (either '| |' or '|||')
	old_position = piece.position
	piece.set_position(position = new_position)

def update_board():
	for i in range(12):
		if A_pieces[i].alive == True:
			my_board[A_pieces[i].position[0]][A_pieces[i].position[1]] = '|%s|' % (A_pieces[i].team)
		if B_pieces[i].alive == True:
			my_board[B_pieces[i].position[0]][B_pieces[i].position[1]] = '|%s|' % (B_pieces[i].team)

# input positions as lists
def check_move(old_position, new_position):
	diagonal_check = [abs(old_position[0] - new_position[0]), abs(old_position[1] - new_position[1])]
	if diagonal_check == [1, 1]:
		return True
	elif diagonal_check == [2, 2]:
		
		# position that piece has "hopped" over
		hopped_position = [1 + min(old_position[0], new_position[0]), 1 + min(old_position[1], new_position[1])]
		
		# find piece that was killed by the "hop"
		i = 0
		while A_pieces[i].position != hopped_position and B_pieces[i].position != hopped_position:
			i += 1

		if A_pieces[i].position == hopped_position:
			A_pieces[i].kill()
		elif B_pieces[i].position == hopped_position:
			B_pieces[i].kill()

		return True
	else:
		print bad_move_error_message
		return False




A_dead = 0
B_dead = 0


# create dictionary of pieces
A_pieces = {}
B_pieces = {}
for i in range(12):
	A_pieces[i] = Piece(team = 'O')
	B_pieces[i] = Piece(team = '*')



# set initial positions of A pieces
k = 0
for i in range(5, 8):
	if i % 2 == 1:
		for j in range(1, 9, 2):
			A_pieces[k].set_position(position = [i,j])
			k += 1
	else:
		for j in range(2, 9, 2):
			A_pieces[k].set_position(position = [i, j])
			k += 1



# set initial positions of B pieces
k = 0
for i in range(0, 3):
	if i % 2 == 1:
		for j in range(1, 9, 2):
			B_pieces[k].set_position(position = [i,j])
			k += 1
	else:
		for j in range(2, 9, 2):
			B_pieces[k].set_position(position = [i, j])
			k += 1



score = '            A: %d       B: %d' %(A_dead, B_dead)
print score

my_board = make_board()
update_board()
os.system('clear')
print_board(my_board)



game = 0
while game == 0:

	my_board = make_board()

	command = str(raw_input('Your move: '))
	# translate command into indexes for old and new positions
	old_position = translate(command[0:2])
	new_position = translate(command[6:])
	
	if check_move(old_position, new_position):
		# find piece that corresponds with old_position
	
		i = 0
		while A_pieces[i].position != old_position and B_pieces[i].position != old_position:
			i += 1

		if A_pieces[i].position == old_position:
			move_piece(A_pieces[i], new_position)
		elif B_pieces[i].position == old_position:
			move_piece(B_pieces[i], new_position)

		update_board()

		os.system('clear')
		score = '            A: %d       B: %d' %(A_dead, B_dead)
		print_board(my_board)




