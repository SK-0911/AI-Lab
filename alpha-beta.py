# Define a function to check if the game is over
def game_over(state):
    # Check for a win on rows, columns, and diagonals
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '-':
            return True
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            return True
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        return True
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        return True

    # Check for a tie
    for row in state:
        if '-' in row:
            return False
    return True


# Define a function to get the possible moves from a game state
def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '-':
                moves.append((i, j))
    return moves


# Define a function to make a move and return a new game state
def make_move(state, move):
    row, col = move
    game_turn = 0;
    player = 'X' if game_turn % 2 == 0 else 'O'
    new_state = [row[:] for row in state]
    new_state[row][col] = player
    return new_state


# Define a function to evaluate a game state
def evaluate_state(state):
    # Check for a win for X
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] == 'X':
            return 10
        if state[0][i] == state[1][i] == state[2][i] == 'X':
            return 10
    if state[0][0] == state[1][1] == state[2][2] == 'X':
        return 10
    if state[0][2] == state[1][1] == state[2][0] == 'X':
        return 10

    # Check for a win for O
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] == 'O':
            return -10
        if state[0][i] == state[1][i] == state[2][i] == 'O':
            return -10
    if state[0][0] == state[1][1] == state[2][2] == 'O':
        return -10
    if state[0][2] == state[1][1] == state[2][0] == 'O':
        return -10

    # Otherwise, the game is not over yet
    return 0


# Define a function to calculate the minimax value of a game state using alpha-beta pruning
def minimax_alpha_beta(state, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over(state):
        return evaluate_state(state)

    if maximizingPlayer:
        max_eval = float("-inf")
        for move in get_possible_moves(state):
            new_state = make_move(state, move)
            eval = minimax_alpha_beta(new_state, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # beta cut-off
        return max_eval

    else:
        min_eval = float("inf")
        for move in get_possible_moves(state):
            new_state = make_move(state, move)
            eval = minimax_alpha_beta(new_state, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # alpha cut-off
        return min_eval


def initial_game_state():
    return [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


# Set the initial game state and other variables
state = initial_game_state()
depth = 4
alpha = float("-inf")
beta = float("inf")
maximizingPlayer = True

# Call the minimax_alpha_beta function to find the best move for the maximizing player
best_move = None
max_eval = float("-inf")
for move in get_possible_moves(state):
    new_state = make_move(state, move)
    eval = minimax_alpha_beta(new_state, depth - 1, alpha, beta, False)
    if eval > max_eval:
        max_eval = eval
        best_move = move
    alpha = max(alpha, eval)

# The best move for the maximizing player is stored in the `best_move` variable

