# Tic-Tac-Toe game


import os

board = ["", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

def main():
    drawboard()
    p = "X"
    while True:                
        while True:
            os.system('cls')
            drawboard()
            print("Player {}'s turn:".format(p))
            try:
                n = int(input("Press 1-9 on keypad: "))
            except ValueError:
               continue

            if 0 < n < 10:
                if board[n] == "_":
                    break
                else:
                    print("Invalid move, try again!")
        if p == "X":
            board[n] = p
        else:
            board[n] = p
        if win():
            os.system('cls')
            drawboard()
            print("Player {} wins!".format(p))
            break
        if not("_" in board):
            os.system('cls')
            drawboard()
            print("DRAW!")
            break
        if p == "X":
            p = "O"
        else:
            p = "X"
    

def drawboard():
    print("\r|{}|{}|{}|".format(board[7], board[8], board[9]))
    print("\r|{}|{}|{}|".format(board[4], board[5], board[6]))
    print("\r|{}|{}|{}|".format(board[1], board[2], board[3]))

def win():
    if (board[7] == board[8] == board[9] == "X" or board[7] == board[8] == board[9] == "O" or
            board[4] == board[5] == board[6] == "X" or board[4] == board[5] == board[6] == "O" or
            board[1] == board[2] == board[3] == "X" or board[1] == board[2] == board[3] == "O" or
            board[7] == board[4] == board[1] == "X" or board[7] == board[4] == board[1] == "O" or
            board[8] == board[5] == board[2] == "X" or board[8] == board[5] == board[2] == "O" or
            board[9] == board[6] == board[3] == "X" or board[9] == board[6] == board[3] == "O" or
            board[7] == board[5] == board[3] == "X" or board[7] == board[5] == board[3] == "O" or
            board[9] == board[5] == board[1] == "X" or board[9] == board[5] == board[1] == "O"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()