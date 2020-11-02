from itertools import cycle
import os
import sys
##########################  Drawing Game-board  ###########################

def draw_board(board):
	col_num = [str(i) for i in range(len(board))]
	print('\n'+'\t'*3+'   '+'   '.join(str(i) for i in col_num))
	count = 0
	for row in board:
		col_items = ''
		for item in row[:len(board)-1]:
			col_items += elem_icon(item)+' | '
		col_items += elem_icon(row[len(board)-1])
		print("\t"*3,count,col_items)
		while count != (len(board)-1):
			print('\t'*3+'   ---------')
			break
		count += 1	


#############################  User Input  ################################

def player_input(input_board, cycle_player):
	print("  Current Player  :", cycle_player)
	row = int(input("\nChoose a row number between (0-2) : "))
	col = int(input("Choose a column number between (0-2) : "))
	try:
		if input_board[row][col] == 0:
			input_board[row][col] = cycle_player
		else:
			print("This position is already taken, try another one")
			player_input(input_board, cycle_player)

	except IndexError as error:
		print("Input position is worng, please try with (0, 1, 2) ", error)
		player_input(input_board, cycle_player)
	except Exception  as error:
		print("Please give your input correctly :( ")
		player_input(input_board, cycle_player)


######################  User Icon  ######################

def elem_icon(by_player):
	if by_player == 1:
		return 'X'
	elif by_player == 2:
		return 'O'
	else :
		return ' '


##################################  Winning Rules  #######################################

def find_win(played_board, player_num):	

	## horizontal match

	for row in played_board:
		hor_index = []
		for col in row:
			hor_index.append(col)
		if all(index == hor_index[0] for index in hor_index) and hor_index[0] != 0:
			print("\nWe got a winner !!    It's :> ",player_num)
			return True
		else:
			continue 

	# Vartical match

	for i in range(3):
		var_index = []
		for j in range(3):
			var_index.append(played_board[j][i])
		if all(index == var_index[0] for index in var_index) and var_index[0] != 0:
			print("\nWe got a winner !!   It's :> ",player_num)
			return True
		else:
			continue

	# diagonal --> Left

	diagonal_left = []
	for i in range(3):
		diagonal_left.append(played_board[i][i])
	if all(index == diagonal_left[0] for index in diagonal_left) and diagonal_left[0] != 0:
		print("\nWe got a winner !!    It's :> ",player_num)
		return True

	# diagonal --> Right

	diagonal_Right = []
	for k in range(len(played_board)):
		for m in range(len(played_board)):
			if k+m == (len(played_board)-1):
				diagonal_Right.append(played_board[k][m])
	if all(index == diagonal_Right[0] for index in diagonal_Right) and diagonal_Right[0] != 0:
		print("\nWe got a winner !!    It's :> ",player_num)
		return True
	else:
		return False


##----------------------- Game Loop ------------------------##

print("\n<<<--------------- Welcome to Tic-Tac-Toe Game ---------------->>>\n")
loop = True
while loop:
	game_board = [[0 for i in range(3)] for j in range(3)]
	player_list = [1 ,2]
	k = cycle(player_list)
	count = 0
	game_loop = True
	while game_loop:			
		player = next(k)
		draw_board(game_board)
		player_input(game_board, player)
		count += 1		
		if find_win(game_board, player) or count == 10:
			if count == 10:
				print("Oops!! This has been drawed ")
			game_loop = False
			choice = input("Would you like to play again ? (y/n) :> ")
			if choice.lower() == 'y' :
				print("\n\t--------- Starting a new game ---------\n")
				loop = True
			elif choice.lower() == 'n':
				print("\n\t*****  Exiting  *****")
				loop = False
			else:
				print("Input Error * Closing the game * ")
				loop = False
		os.system('cls')

sys.stdin.readline()