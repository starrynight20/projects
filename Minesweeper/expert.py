import random
import pyautogui
import time
from universal_funcs import check_if_won as check_if_won
from universal_funcs import clear_screen as clear_screen
from universal_funcs import sleep as sleep
from universal_funcs import score_saver_expert as score_saver_expert

def fake_expert_board():

    fake_expert_board = [['-' for row in range(30)] for column in range(16)]

    real_expert_board = [[0 for row in range(30)] for column in range(16)]

    for number in range(99):
        y = random.randint(0, 15)
        x = random.randint(0, 29)

        if real_expert_board[y][x] != 'X':
            real_expert_board[y][x] = 'X'

        elif real_expert_board[y][x] == 'X':
            for cell in real_expert_board[y][x]:
                if cell != 'X':
                    real_expert_board[y][cell] = 'X'

        if (0 <= x <= 28) and (0 <= y <= 15):
            if real_expert_board[y][x + 1] != 'X':
                real_expert_board[y][x + 1] += 1

        if (1 <= x <= 29) and (0 <= y <= 15):
            if real_expert_board[y][x - 1] != 'X':
                real_expert_board[y][x - 1] += 1

        if (1 <= x <= 28) and (1 <= y <= 14):
            if real_expert_board[y - 1][x - 1] != 'X':
                real_expert_board[y - 1][x - 1] += 1

        if (0 <= x <= 27) and (1 <= y <= 14):
            if real_expert_board[y - 1][x + 1] != 'X':
                real_expert_board[y - 1][x + 1] += 1

        if (0 <= x <= 28) and (1 <= y <= 14):
            if real_expert_board[y - 1][x] != 'X':
                real_expert_board[y - 1][x] += 1

        if (0 <= x <= 27) and (0 <= y <= 13):
            if real_expert_board[y + 1][x + 1] != 'X':
                real_expert_board[y + 1][x + 1] += 1

        if (1 <= x <= 28) and (0 <= y <= 13):
            if real_expert_board[y + 1][x - 1] != 'X':
                real_expert_board[y + 1][x - 1] += 1

        if (0 <= x <= 28) and (0 <= y <= 13):
            if real_expert_board[y + 1][x] != 'X':
                real_expert_board[y + 1][x] += 1

    start = time.time()

    while not check_if_won(fake_expert_board):
        try:

            for row in fake_expert_board:
                print(" ".join(str(cell) for cell in row))

            y = int(input("Y - 0 to 98\n"))
            x = int(input("X - 0 to 98\n"))
            flag = input("Flag? y/n/u\n")

            if flag == 'y':
                fake_expert_board[y][x] = 'F'
                clear_screen()

            elif flag == 'n':
                fake_expert_board[y][x] = real_expert_board[y][x]
                clear_screen()

            elif flag == 'u':
                fake_expert_board[y][x] = '-'
                clear_screen()

            if real_expert_board[y][x] == 'X' and flag == 'n':
                for row in fake_expert_board:
                    print(" ".join(str(cell) for cell in row))

                print("Mine! You lost")
                sleep(1.5)
                quit()

        except ValueError:
            pass

        except IndexError:
            print('The number 99 is not a valid option')
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
        score_saver_expert(final)