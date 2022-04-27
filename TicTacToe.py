# assignment : TicTacToe.py
# aurthor: sydney mangwana
# date : 12 Jan 2022

def main():
    board = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}

    print(printtheboard(board))

    # loop will iterate as long as the boolean value for boardcompleted is False
    p = ""
    while not (gameover(board) or winning_combination(board)):
        p = next_player(p)
        board = player_Input(p, board)
        print()
        print(printtheboard(board))
        print()

    print("Thank you for playing the game")


def printtheboard(theboard):
    print()
    print(theboard[1] + '|' + theboard[2] + '|' + theboard[3])
    print("-+-+-")
    print(theboard[4] + '|' + theboard[5] + '|' + theboard[6])
    print("-+-+-")
    print(theboard[7] + '|' + theboard[8] + '|' + theboard[9])
    print()

# current player chooses a position on the grid


def player_Input(player, fromdictionary):
    position = int(input(f"Player {player}'s turn to play (1-9) : "))
    fromdictionary[position] = player.upper()
    updateddictionary = fromdictionary
    return updateddictionary


# determine who is playing next
def next_player(currentplayer):
    if currentplayer == "" or currentplayer == "O":
        return "X"
    else:
        return "O"


# check if the board is filled or not
def gameover(fromdictionary):
    for c in range(1, 10):
        if fromdictionary[c] != 'X' and fromdictionary[c] != 'O':
            return False
    return True


# check if a player has won.
def winning_combination(fromboard):
    if fromboard[1] == fromboard[2] and fromboard[2] == fromboard[3]:
        return True
    elif fromboard[4] == fromboard[5] and fromboard[5] == fromboard[6]:
        return True
    elif fromboard[7] == fromboard[8] and fromboard[8] == fromboard[9]:
        return True
    elif fromboard[1] == fromboard[4] and fromboard[4] == fromboard[7]:
        return True
    elif fromboard[2] == fromboard[5] and fromboard[5] == fromboard[8]:
        return True
    elif fromboard[3] == fromboard[6] and fromboard[6] == fromboard[9]:
        return True
    elif fromboard[1] == fromboard[5] and fromboard[5] == fromboard[9]:
        return True
    elif fromboard[3] == fromboard[5] and fromboard[5] == fromboard[7]:
        return True


if __name__ == "__main__":
    main()
