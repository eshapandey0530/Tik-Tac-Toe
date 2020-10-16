board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

current = 'X'

game_contiue = True

def display():
    print(board[0], ' | ', board[1], ' | ', board[2])
    print('-------------')
    print(board[3], ' | ', board[4], ' | ', board[5])
    print('-------------')
    print(board[6], ' | ', board[7], ' | ', board[8])

def choose_position():
    position = int(input('Choose a position(1-9): '))
    if board[position-1] == ' ':
        return position
    else:
        print('Already occupied! Choose another number')
        return choose_position()

def row_winner():
    if board[0]==board[1]==board[2]!=' ':
        return True, board[0]
    elif board[3]==board[4]==board[5]!=' ':
        return True, board[3]
    elif board[6]==board[7]==board[8]!=' ':
        return True, board[6]
    else:
        return False, None

def column_winner():
    if board[0] == board[3] == board[6] != ' ':
        return True, board[0]
    elif board[1] == board[4] == board[7] != ' ':
        return True, board[1]
    elif board[2] == board[5] == board[8] != ' ':
        return True, board[2]
    else:
        return False, None

def diagonal_winner():
    if board[0] == board[4] == board[8] != ' ':
        return True, board[0]
    elif board[2] == board[4] == board[6] != ' ':
        return True, board[2]
    else:
        return False, None

def check_tie():
    count=0
    for i in board:
        if i != ' ':
            count+=1
    if count==9:
        return True
    else:
        return False

def check_winner():
    row, value1 = row_winner()
    column, value2 = column_winner()
    diagonal, value3 = diagonal_winner()
    tie = check_tie()
    if row==True:
        display()
        print(value1,' wins')
    elif column==True:
        display()
        print(value2,' wins')
    elif diagonal==True:
        display()
        print(value3,' wins')
    elif tie==True:
        display()
        print("It's a Tie")
    else:
        game()

def change_turn():
    global current
    if current=='X':
        current='O'
    else:
        current='X'

def game():
    #global board
    display()
    print(current,"'s turn")
    #ask for position
    n=choose_position()
    #set value in board
    board[n - 1] = current
    #change player
    change_turn()
    #choose winner
    check_winner()

if __name__ == '__main__':
    game()
