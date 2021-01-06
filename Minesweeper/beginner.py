import random
import pyautogui
import time
from universal_funcs import check_if_won as check_if_won
from universal_funcs import clear_screen as clear_screen
from universal_funcs import sleep as sleep
from universal_funcs import score_saver_beginner as score_saver_beginner

def fake_beginner_board():

    fake_board = [['-' for row in range(9)] for column in range(9)]

    real_board = [[0 for row in range(9)] for column in range(9)]

    for number in range(10):
        y = random.randint(0, 8)
        x = random.randint(0, 8)

        if real_board[y][x] != 'X':
            real_board[y][x] = 'X'

        elif real_board[y][x] == 'X':
            for cell in real_board[y][x]:
                if cell != 'X':
                    real_board[y][cell] = 'X'

        if (0 <= x <= 7) and (0 <= y <= 8):
            if real_board[y][x + 1] != 'X':
                real_board[y][x + 1] += 1

        if (1 <= x <= 8) and (0 <= y <= 8):
            if real_board[y][x - 1] != 'X':
                real_board[y][x - 1] += 1

        if (1 <= x <= 7) and (1 <= y <= 7):
            if real_board[y - 1][x - 1] != 'X':
                real_board[y - 1][x - 1] += 1

        if (0 <= x <= 6) and (1 <= y <= 7):
            if real_board[y - 1][x + 1] != 'X':
                real_board[y - 1][x + 1] += 1

        if (0 <= x <= 7) and (1 <= y <= 7):
            if real_board[y - 1][x] != 'X':
                real_board[y - 1][x] += 1

        if (0 <= x <= 6) and (0 <= y <= 6):
            if real_board[y + 1][x + 1] != 'X':
                real_board[y + 1][x + 1] += 1

        if (1 <= x <= 7) and (0 <= y <= 6):
            if real_board[y + 1][x - 1] != 'X':
                real_board[y + 1][x - 1] += 1

        if (0 <= x <= 7) and (0 <= y <= 6):
            if real_board[y + 1][x] != 'X':
                real_board[y + 1][x] += 1

    start = time.time()

    while not check_if_won(fake_board):
        try:

            for row in fake_board:
                print(" ".join(str(cell) for cell in row))

            y = int(input("Y - 0 to 8\n"))
            x = int(input("X - 0 to 8\n"))
            flag = input("Flag? y/n/u\n")

            if flag == 'y':
                if fake_board[y][x] != '-':
                    print("Can't flag a number")

                else:
                    fake_board[y][x] = 'F'

                clear_screen()

            elif flag == 'n':
                fake_board[y][x] = real_board[y][x]
                clear_screen()

            elif flag == 'u':
                fake_board[y][x] = '-'
                clear_screen()

            if real_board[y][x] == 'X' and flag == 'n':
                for row in fake_board:
                    print(" ".join(str(cell) for cell in row))

                print("Mine! You lost")
                sleep(1.5)
                quit()

        except ValueError:
            pass

        except IndexError:
            print('The number 9 is not a valid option')
            sleep(1.5)
            clear_screen()
            pass

    else:
        end = time.time()
        temp = end - start
        minutes = temp // 60
        seconds = temp - 60 * minutes
        final = '%d\n' % seconds
        print('You won!')
        print(final)
        print('Saving your score....')
        score_saver_beginner(final)
