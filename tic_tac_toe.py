class CustomError(Exception):
    """
        This is a custom error for testing if the symbol the player chooses is either 'X' or 'O'
    """
    pass


def display_board(x):
    """
        This function displays the current state of the board.
    :param x: the list of symbols already chosen
    :return: Nothing
    """
    board = [[f'\t {x[i+0]} \t', '|', f'\t {x[i+1]} \t', '|', f'\t {x[i+2]}'] for i in [0, 3, 6]]
    print(''.join(board[2]))
    print(''.join(board[1]))
    print(''.join(board[0]))


def create_new_board():
    """
    Creates an empty list of moves.
    :return: empty list of moves
    """
    return 9 * [' ']


def player2_move(x, p2):
    """
        Actions taken during the 2nd player turn
    :param x: List of the current state of the board
    :param p2: symbol of the player 2
    :return:
    """
    i = int(input("Player 2, please choose your next position: (1-9) \t"))
    if x[i-1] != ' ':
        raise Custom_Error

    x[i-1] = p2
    display_board(x)


def player1_move(x, p1):
    """
        Actions taken during the 2nd player turn
    :param x: List of the current state of the board
    :param p1: symbol of the player 1
    :return:
    """
    i = int(input("Player 1, please choose your next position: (1-9) \t"))
    if x[i-1] != ' ':
        raise Custom_Error

    x[i-1] = p1
    display_board(x)


def is_game_over(x):
    """
        Checks if the game is over
    :param x: current state of the board
    :return: A boolean of if the game is finished or not
    """
    for i in [0, 3, 6]:
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
    """
        Asks the players if they want to play again
    :return: Player answer
    """
    a = input("Do you want to play again ?  (y/n) \t ")
    return a == 'y'


def main():
    """
        Main development of the game
    :return: Nothing
    """
    play = True
    print("Welcome to Tic_Tac_Toe")
    p1 = input("Would you like to play as 'X' or 'O' ?  ").upper()
    try:
        assert p1 in ['X', 'O']
    except AssertionError:
        p1 = 'X'
        print("Your input was invalid, you are 'X' by default")
    p2 = 'X' if p1 == 'O' else 'O'

    while play:
        x = create_new_board()
        print("These are the spots numbers from 1 to 9 refer to")
        display_board([1, 2, 3, 4, 5, 6, 7, 8, 9])
        while True:

            while True:
                try:
                    player1_move(x, p1)
                except CustomError:
                    print("You chose a spot already taken, please pick a free spot")
                except (IndexError, ValueError):
                    print("Your input is invalid."
                          " \n  Please enter a number between 1 and 9 corresponding to an empty space of the board")
                else:
                    break

            if is_game_over(x):
                print(" Congratulations player 1, you won !")
                break

            if ' ' not in x:
                print("It is a tie !")
                break

            while True:
                try:
                    player2_move(x, p2)
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


if __name__ == "__main__":
    main()
