global player
player = 1

def draw():
    for row in board:
        print(row)

def pick_cell():
    while True:
        try:
            global player

            horizontal_victory()
            vertical_victory()
            diagonal_victory()
            filled_cells()

            if player == 1:
                choice = int(input("Where would Player 1 like to play?"))
                if valid_number(choice) and available(choice):
                    place(choice, player)
                    player += 1
                    draw()

            elif player == 2:
                choice = int(input("Where would Player 2 like to play?"))
                if valid_number(choice) and available(choice):
                    place(choice, player)
                    player -= 1
                    draw()

        except ValueError:
            print("That's not a number")

def valid_number(number):
    if number in range(1, 10):
        return True
    else:
        return False

def place(number, player):
    if player == 1:
        if number == 1:
            board[0][0] = 'X'
        elif number == 2:
            board[0][1] = 'X'
        elif number == 3:
            board[0][2] = 'X'
        elif number == 4:
            board[1][0] = 'X'
        elif number == 5:
            board[1][1] = 'X'
        elif number == 6:
            board[1][2] = 'X'
        elif number == 7:
            board[2][0] = 'X'
        elif number == 8:
            board[2][1] = 'X'
        elif number == 9:
            board[2][2] = 'X'

    elif player == 2:
        if number == 1:
            board[0][0] = 'O'
        elif number == 2:
            board[0][1] = 'O'
        elif number == 3:
            board[0][2] = 'O'
        elif number == 4:
            board[1][0] = 'O'
        elif number == 5:
            board[1][1] = 'O'
        elif number == 6:
            board[1][2] = 'O'
        elif number == 7:
            board[2][0] = 'O'
        elif number == 8:
            board[2][1] = 'O'
        elif number == 9:
            board[2][2] = 'O'

def filled_cells():

    spaces = 9

    for element in board[0]:
        if element != ".":
            spaces -= 1
    for element in board[1]:
        if element != ".":
            spaces -= 1
    for element in board[2]:
        if element != ".":
            spaces -= 1

    if spaces == 0:
        print("All the spaces are filled, no one won!")
        quit()

def horizontal_victory():
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][0] == 'O':
            print("PLayer 2 won!")
            quit()

    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] == 'X':
            print("Player 1 won!")
            quit()

        elif board[1][0] == 'O':
            print("Player 2 won!")
            quit()

    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] == 'X':
            print("Player 1 won!")
            quit()

        elif board[2][0] == 'O':
            print("Player 2 won!")
            quit()

def vertical_victory():
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][0] == 'X':
            print("Player 2 won!")
            quit()

    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][1] == 'O':
            print("Player 2 won!")
            quit()

    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][2] == 'O':
            print("Player 2 won!")
            quit()

def diagonal_victory():
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][0] == 'O':
            print("Player 2 won!")
            quit()

    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            print("Player 1 won!")
            quit()

        elif board[0][2] == 'O':
            print("Player 2 won!")
            quit()

def available(x):
    if x == 1:
        if board[0][0] == ".":
            return True
        else:
            print("Spot is taken")
            return False
    elif x == 2:
        if board[0][1] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 2:
        if board[0][1] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 3:
        if board[0][2] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 4:
        if board[1][0] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 5:
        if board[1][1] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 6:
        if board[1][2] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 7:
        if board[2][0] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 8:
        if board[2][1] == ".":
            return True
        else:
            print("Spot is taken")
            return False

    elif x == 9:
        if board[2][2] == ".":
            return True
        else:
            print("Spot is taken")
            return False

cell0, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8 = ".", ".", ".", ".", ".", ".", ".", ".", ".",

board = [[cell0, cell1, cell2],
         [cell3, cell4, cell5],
         [cell6, cell7, cell8]]

draw()
pick_cell()