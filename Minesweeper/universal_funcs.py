import time
import pyautogui

def sleep(x):
    time.sleep(x)

def clear_screen():
    pyautogui.hotkey('ctrl', 'l')

def check_if_won(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def score_saver_beginner(x):
    f = open("scores_beginner.txt", "a+")
    f.write(x)
    f.close()
    quit()

def score_saver_intermediate(x):
    f = open("scores_intermediate.txt", "a+")
    f.write(x)
    f.close()
    quit()

def score_saver_expert(x):
    f = open("scores_expert.txt", "a+")
    f.write(x)
    f.close()
    quit()
