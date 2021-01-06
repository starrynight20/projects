import random
import pyautogui
import time
from universal_funcs import check_if_won as check_if_won
from universal_funcs import clear_screen as clear_screen
from universal_funcs import sleep as sleep
from universal_funcs import score_saver_intermediate as score_saver_intermediate

def fake_intermediate_board():

    fake_intermediate_board = [['-' for row in range(16)] for column in range(16)]

    real_intermediate_board = [[0 for row in range(16)] for column in range(16)]

    for number in range(16):
        y = random.randint(0, 15)
        x = random.randint(0, 15)

        if real_intermediate_board[y][x] != 'X':
            real_intermediate_board[y][x] = 'X'

        elif real_intermediate_board[y][x] == 'X':
            for cell in real_intermediate_board[y][x]:
                if cell != 'X':
                    real_intermediate_board[y][cell] = 'X'

        if (0 <= x <= 14) and (0 <= y <= 15):
            if real_intermediate_board[y][x + 1] != 'X':
                real_intermediate_board[y][x + 1] += 1

        if (1 <= x <= 15) and (0 <= y <= 15):
            if real_intermediate_board[y][x - 1] != 'X':
                real_intermediate_board[y][x - 1] += 1

        if (1 <= x <= 14) and (1 <= y <= 14):
            if real_intermediate_board[y - 1][x - 1] != 'X':
                real_intermediate_board[y - 1][x - 1] += 1

        if (0 <= x <= 13) and (1 <= y <= 14):
            if real_intermediate_board[y - 1][x + 1] != 'X':
                real_intermediate_board[y - 1][x + 1] += 1

        if (0 <= x <= 14) and (1 <= y <= 14):
            if real_intermediate_board[y - 1][x] != 'X':
                real_intermediate_board[y - 1][x] += 1

        if (0 <= x <= 13) and (0 <= y <= 13):
            if real_intermediate_board[y + 1][x + 1] != 'X':
                real_intermediate_board[y + 1][x + 1] += 1

        if (1 <= x <= 14) and (0 <= y <= 13):
            if real_intermediate_board[y + 1][x - 1] != 'X':
                real_intermediate_board[y + 1][x - 1] += 1

        if (0 <= x <= 14) and (0 <= y <= 13):
            if real_intermediate_board[y + 1][x] != 'X':
                real_intermediate_board[y + 1][x] += 1

    start = time.time()

    while not check_if_won(fake_intermediate_board):
        try:

            for row in fake_intermediate_board:
                print(" ".join(str(cell) for cell in row))

            y = int(input("Y - 0 to 15\n"))
            x = int(input("X - 0 to 15\n"))
            flag = input("Flag? y/n/u\n")

            if flag == 'y':
                if fake_intermediate_board[y][x] != '-':
                    print("Can't flag a number")

                else:
                    fake_intermediate_board[y][x] = 'F'

                clear_screen()

            elif flag == 'n':
                fake_intermediate_board[y][x] = real_intermediate_board[y][x]
                clear_screen()

            elif flag == 'u':
                fake_intermediate_board[y][x] = '-'
                clear_screen()

            if real_intermediate_board[y][x] == 'X' and flag == 'n':
                for row in fake_intermediate_board:
                    print(" ".join(str(cell) for cell in row))

                print("Mine! You lost")
                sleep(1.5)
                quit()

        except ValueError:
            pass

        except IndexError:
            print('The number 16 is not a valid option')
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
        score_saver_intermediate(final)
