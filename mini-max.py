# Define the initial game state
game_state = [
    ['X', '-', '-'],
    ['-', 'O', '-'],
    ['X', '-', '-']
]

# Define a function to check if the game is over
def game_over(state):
    # Check rows for a win
    for row in state:
        if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
            return True
    # Check columns for a win
    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            return True
    # Check diagonals for a win
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        return True
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        return True
    # Check for a tie game
    for row in state:
        if '-' in row:
            return False
    return True

# Define a function to get the possible moves for a player
def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '-':
                moves.append((i, j))
    return moves

# Define a function to make a move for a player
def make_move(state, move, player):
    i, j = move
    new_state = [row.copy() for row in state]
    new_state[i][j] = player
    return new_state

# Define a function to evaluate the state of the game for a player
def evaluate_state(state):
    # Check rows for a win
    for row in state:
        if row == ['X', 'X', 'X']:
            return 10
        elif row == ['O', 'O', 'O']:
            return -10
    # Check columns for a win
    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            if state[0][i] == 'X':
                return 10
            else:
                return -10
    # Check diagonals for a win
    if state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        if state[0][0] == 'X':
            return 10
        else:
            return -10
    if state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        if state[0][2] == 'X':
            return 10
        else:
            return -10
    # Return 0 if game is not over
    if not game_over(state):
        return 0
    # Return a tie score if game is over and no winner
    return 0


# Define the Mini-Max algorithm
def mini_max(state, player):
    # Check if game is over
    if game_over(state):
        return evaluate_state(state), None
    # Get the possible moves
    moves = get_possible_moves(state)
    # Initialize the best score and best move
    if player == 'X':
        best_score = -float('inf')
    else:
        best_score = float('inf')
    best_move = None
    # Loop through the possible moves
    for move in moves:
        # Make the move
        new_state = make_move(state, move, player)
        # Recursively call mini_max for the opposite player
        if player == 'X':
            score, _ = mini_max(new_state, 'O')
        else:
            score, _ = mini_max(new_state, 'X')
        # Update the best score and best move
        if player == 'X':
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    return best_score, best_move

# Test the Mini-Max algorithm with an example game state


best_score, best_move = mini_max(game_state, 'O')

print('Best move:', best_move)
print('Best score:', best_score)

