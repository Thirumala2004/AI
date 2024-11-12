import random

def choice():
    ch = input("Do you want to play first : ")
    if ch.lower().startswith('n'):
        return [3,5]  # 3 for human, 5 for computer
    return [5,3]

def isEmpty(board, i):
    if board[i] == 2:
        return True

def chooseRandom(b, moveList):
    possible = []
    for i in moveList:
        if isEmpty(b, i):
            possible.append(i)
    if len(possible) != 0:
        return random.choice(possible)
    else:
        return None

def makeMove(b, player, pos):
    b[pos] = player

def isWinner(b, p):
    # Check all possible winning combinations
    if b[1]==b[2]==b[3]==p:
        return True
    elif b[4]==b[5]==b[6]==p:
        return True
    elif b[7]==b[8]==b[9]==p:
        return True
    elif b[1]==b[4]==b[7]==p:
        return True
    elif b[2]==b[5]==b[8]==p:
        return True
    elif b[3]==b[6]==b[9]==p:
        return True
    elif b[1]==b[5]==b[9]==p:
        return True
    elif b[3]==b[5]==b[7]==p:
        return True
    else:
        return False

def hmove(board):
    pos = int(input("Enter Position : "))
    if isEmpty(board, pos):
        return pos
    return hmove(board)

def cmove(h, c, board):
    # Check if computer can win
    for i in range(1, 10):
        cpy = board.copy()
        if isEmpty(board, i):
            makeMove(cpy, c, i)
            if isWinner(cpy, c):
                return i
    # Check if human can win and block
    for i in range(1, 10):
        cpy = board.copy()
        if isEmpty(board, i):
            makeMove(cpy, h, i)
            if isWinner(cpy, h):
                return i
    # Choose a corner
    move = chooseRandom(board, [1, 3, 7, 9])
    if move!=None:
        return move
    # Choose center
    if isEmpty(board, 5):
        return 5
    # Choose side
    return chooseRandom(board, [2, 4, 6, 8])

def draw(board):
    for i in range(1, 10):
        if i in [3, 6, 9]:
            if board[i] == 3:
                print('O')
            elif board[i] == 5:
                print('X')
            else:
                print('_')
        else:
            if board[i] == 3:
                print('O', end=' ')
            elif board[i] == 5:
                print('X', end=' ')
            else:
                print('_', end=' ')
    print()

def main():
    print("Welcome to the Game")
    board = [2] * 10  # Initialize board with empty spots (index 0 is unused)
    h, c = choice()  # Decide who goes first
    player = h if h > c else c  # Set the initial player

    for turn in range(1, 10):  # Max 9 moves in Tic-Tac-Toe
        if player == h:  # Human's turn
            move = hmove(board)
            makeMove(board, player, move)
            draw(board)
            if isWinner(board, player):
                print("you won!")
                break
            player = c
        else:  # Computer's turn
            move = cmove(h, c, board)
            makeMove(board, player, move)
            draw(board)
            if isWinner(board, player):
                print("you lose.")
                break
            player = h
        if turn == 9:
            print("The game is a tie.")

if __name__ == "__main__":
    main()
