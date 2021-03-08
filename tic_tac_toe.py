#defines dsplay_board to display the board when needed
def display_board(board):
    #prints out first row of the board
    #numbers are assigned to each space to allow player moves
    print(" {0} | {1} | {2} ".format(board[0],board[1],board[2]))
    print("-----------")
    #prints out second row of the board
    print(" {0} | {1} | {2} ".format(board[3],board[4],board[5]))
    print("-----------")
    #prints out third row of the board
    print(" {0} | {1} | {2} ".format(board[6],board[7],board[8]))
#defines get_player_input for player moves
def get_player_input(board):
    #if = False the loop will execute, if = True the loop will not
    valid_move = False
    while not valid_move:
        #assigns move to player input
        move = int(input("Where would you like to move?"))
        #move is greater than or = to 0 and also less than or = the 8 a board number will be relpaced with an X or an O depending on the player turn 
        if move >=0 and move <=8 and board[move] not in ('X','O'):
            #it thhen is a vaild move and is inserted into the board
            valid_move = True
        #move is stored in the board
    return move
    
#defines a way to update the board
def update_board(board,move,p1_turn):
    #this say if player 1 has put his input in then a X will be printed
    if p1_turn:
        board[move] = 'X'
        #if player 2 has put in input or not player 1 a O will be printed
    else:
        board[move] = 'O'
#defines a way to check for a win
def check_for_win(board):
    #if found_winner = False the if statements will run until found_winner = True
    found_winner = False
    #all ifs and elif are saying if the three values that are up,down,side to side or diagonal are = ,found_winner will be True
    if board[0] == board[1] == board[2]:
        found_winner = True
    elif board[3] == board[4] == board[5]:
        found_winner = True
    elif board[6] == board[7] == board[8]:
        found_winner = True
    elif board[0] == board[3] == board[6]:
        found_winner = True
    elif board[1] == board[4] == board[7]:
        found_winner = True
    elif board[2] == board[5] == board[8]:
        found_winner = True
    elif board[0] == board[4] == board[8]:
        found_winner = True
    elif board[2] == board[4] == board[6]:
        found_winner = True
        #when found_winner = True the game will end and the program will know
    return found_winner
#defines a way to check for a tie
def check_for_tie(board):
    #the number of X's and O's in the playing = 0
    count_XO = 0
    #space now = the empty space's in the playing board
    for space in board:
        #if the space is filled with an X or a O, 1 will be added to the count
        if space == 'X' or space == 'O':
            count_XO += 1
#if the count = nine a tie will be found, if count dose not = nine, itt is not a tie
    if count_XO == 9:
        return True
    else:
        return False
    
    
#main chunk of code
def main():
    #creates a list for the spaces on the borad to be displayed in numbers
    board = ['0','1','2','3','4','5','6','7','8']
    #player 1 get first move
    p1_turn = True
    #no winner is found
    found_winner = False
    #no tie is found
    found_tie = False
#while found_winner = False and found_tie = False, the loop will run
    while not (found_winner or found_tie):
        #displays board as defined earlier
        display_board(board)
        #gets player input as defined earlier
        move = get_player_input(board)
        #updates board as defined earlier
        update_board(board, move, p1_turn)
        #looks for winner as defined earlier
        found_winner = check_for_win(board)
        #if no winner is found, check for tie, as defined earlier, is execute
        if not found_winner:
            found_tie = check_for_tie(board)
            #switchs turns to p2 or next player
        p1_turn = not p1_turn
#displays board as defined earlier
    display_board(board)
    #if found_winner = True, "Congratulations! You won!" will be printed to the screen
    if found_winner:
        print("Congratulations! You won!")
        #if no winner is found the game is a tie
    else:
        print("This game ended in a tie.")

    
main()
