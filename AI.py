# Tic Tac Toe with Minimax + Alpha Beta Pruning

PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# BOARD FUNCTIONS 

def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")
    print()

def is_moves_left(board):
    return EMPTY in board

def check_winner(board):
    winning_combinations = [
        (0,1,2),(3,4,5),(6,7,8),  
        (0,3,6),(1,4,7),(2,5,8),  
        (0,4,8),(2,4,6)           
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None

#  MINIMAX WITH ALPHA-BETA 

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)

    if winner == AI:
        return 10 - depth
    if winner == PLAYER:
        return depth - 10
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def best_move(board):
    best_val = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_val = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# GAME LOOP 

def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O")
    print("Positions are 1 to 9 as shown below:")

    sample = ['1','2','3','4','5','6','7','8','9']
    print_board(sample)

    while True:
        print_board(board)

        # Player move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[move] = PLAYER

        if check_winner(board) == PLAYER:
            print_board(board)
            print("🎉 You win!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = AI
        print("Computer played:", ai_move + 1)

        if check_winner(board) == AI:
            print_board(board)
            print("💻 Computer wins!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

# ---------------- START ---------------- #

play_game()
