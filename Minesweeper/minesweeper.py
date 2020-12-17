import time
import beginner
import intermediate
import expert
from universal_funcs import clear_screen as clear_screen
from universal_funcs import sleep as sleep

def main_menu():
    print("Welcome to minesweeper")
    sleep(2)
    print("To play the game, input 1.\n"
          "To look at the scoreboard, input 2.\n"
          "To read the game instructions, input 3.\n"
          "To quit, input 4")

    while True:
        try:
            choice = int(input("\nWhere would you like to go?\n"))

            if choice in range(1, 5):
                main_menu_choice(choice)

            else:
                print("Invalid option")
                sleep(2)
                clear_screen()
                main_menu()

        except ValueError:
            print("Invalid option")
            sleep(2)
            clear_screen()
            main_menu()

def main_menu_choice(x):
    if x == 1:
        print("Loading up the game...")
        sleep(2)
        clear_screen()
        print("What category would you like to play?\n"
              " Input 1 for Beginner\n "
              "Input 2 for Intermediate \n "
              "Input 3 for Expert")

        while True:
            try:
                category = int(input("\n"))

                if category in range(1, 4):

                    if category == 1:
                        clear_screen()
                        beginner.fake_beginner_board()

                    elif category == 2:
                        clear_screen()
                        intermediate.fake_intermediate_board()

                    elif category == 3:
                        clear_screen()
                        expert.fake_expert_board()

                else:
                    print("Not an option")
                    sleep(2)
                    clear_screen()
                    main_menu()

            except ValueError:
                pass

    elif x == 2:
        clear_screen()

        while True:
            try:
                print("What scoreboard would you like to print?\n"
                      "Input 1 for Beginner\n"
                      "Input 2 for Intermediate\n"
                      "Input 3 for Expert\n"
                      "Input 4 to go back to the main menu\n")

                scoreboard_choice = int(input(''))
                clear_screen()

                if scoreboard_choice == 1:
                    f = open('scores_beginner.txt', 'r')
                    file_contents = f.read()
                    print("Beginner scoreboard")
                    clear_screen()
                    print(file_contents)
                    f.close()

                elif scoreboard_choice == 2:
                    f = open('scores_intermediate.txt', 'r')
                    file_contents = f.read()
                    print("Intermediate scoreboard")
                    clear_screen()
                    print(file_contents)
                    f.close()

                elif scoreboard_choice == 3:
                    f = open('scores_expert.txt', 'r')
                    file_contents = f.read()
                    print('Expert scoreboard')
                    clear_screen()
                    print(file_contents)
                    f.close()

                elif scoreboard_choice == 4:
                    main_menu()

            except ValueError:
                pass

    elif x == 3:
        print("Loading instructions...")
        sleep(2)
        clear_screen()
        print(" You are presented with a board of squares. Some squares contain mines (bombs), others don't.\n If you click on a square containing a bomb, you lose.\n If you manage to click all the squares (without clicking on any bombs) you win.\n"
              " Clicking a square which doesn't have a bomb reveals the number of neighbouring squares containing bombs.\n Use this information plus some guess work to avoid the bombs.")
        print("\nTo go back, input 1")

        while True:
            try:
                go_back_2 = int(input(''))

                if go_back_2 == 1:
                    clear_screen()
                    main_menu()

            except ValueError:
                pass

    elif x == 4:
        clear_screen()
        print("Quitting...")
        sleep(1)
        quit()

#Categories:
#Beginner ( 9 x 9, 10 )
#Intermediate ( 16 x 16, 30 )
#Expert ( 16 x 30, 99 )

main_menu()