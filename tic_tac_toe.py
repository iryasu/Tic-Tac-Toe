class Custom_Error(Exception):
    pass


def display_board(x):
    board = [[f'\t {x[i+0]} \t', '|', f'\t {x[i+1]} \t', '|', f'\t {x[i+2]}'] for i in [0,3,6]]
    print(''.join(board[2]))
    print(''.join(board[1]))
    print(''.join(board[0]))


def create_new_board():
    return 9 * [' ']


def player2_move(x, p2):
    i = int(input("Player 2, please choose your next position: (1-9) \t"))
    if x[i-1] != ' ':
        raise Custom_Error

    x[i-1] = p2
    display_board(x)


def player1_move(x, p1):
    i = int(input("Player 1, please choose your next position: (1-9) \t"))
    if x[i-1] != ' ':
        raise Custom_Error

    x[i-1] = p1
    display_board(x)


def is_game_over(x):
    for i in [0,3,6]:
        if x[i] == x[i+1] and x[i] == x[i+2] and x[i] != ' ':
            return True
    for i in range(3):
        if x[i] == x[i + 3] and x[i] == x[i + 6] and x[i] != ' ':
            return True
    if x[0] == x[4] and x[0] == x[8] and x[0] != ' ':
        return True
    if x[2] == x[4] and x[2] == x[6] and x[2] != ' ':
        return True
    return False


def play_again():
    a = input("Do you want to play again ?  (y/n) \t ")
    return a == 'y'

def main():
    play = True
    winner = None
    print("Welcome to Tic_Tac_Toe")
    p1 = input("Would you like to play as 'X' or 'O' ?  ")
    try:
        assert p1 in ['X','O']
    except AssertionError:
        p1 = 'X'
        print("Your input was invalid, you are 'X' by default")
    p2 = 'X' if p1 == 'O' else 'O'


    while(play):
        game_over = False
        x = create_new_board()
        print("These are the spots numbers from 1 to 9 refer to")
        display_board([1,2,3,4,5,6,7,8,9])
        while(not game_over):

            while True:
                try:
                    player1_move(x,p1)
                except Custom_Error:
                    print("You chose a spot already taken, please pick a free spot")
                except (IndexError, ValueError):
                    print("Your input is invalid."
                          " \n  Please enter a number between 1 and 9 corresponding to an empty space of the board")
                else:
                    break

            game_over = is_game_over(x)
            if game_over == True:
                print(" Congratulations player 1, you won !")
                break

            if ' ' not in x:
                print("It is a tie !")
                break

            while True:
                try:
                    player2_move(x,p2)
                except Custom_Error:
                    print("You chose a spot already taken, please pick a free spot")
                except (IndexError, ValueError):
                    print("Your input is invalid."
                          " \n  Please enter a number between 1 and 9 corresponding to an empty space of the board")
                else:
                    break

            game_over = is_game_over(x)
            if game_over:
                print(" Congratulations player 2, you won !")

            if ' ' not in x:
                print("It is a tie !")
                break
        play = play_again()

main()