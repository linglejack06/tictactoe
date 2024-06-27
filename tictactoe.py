"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for space in row:
            if space == X:
                x_count += 1
            elif space == O:
                o_count += 1

    if x_count > o_count:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedBoard = copy.deepcopy(board)
    if copiedBoard[action[0]][action[1]] == EMPTY:
        if player(copiedBoard) == X:
            copiedBoard[action[0]][action[1]] = X
        else:
            copiedBoard[action[0]][action[1]] = O
        return copiedBoard
    else:
        raise Exception("Action not available")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check for horizontal win
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return X
        elif row[0] == row[1] == row[2] == O:
            return O

    # check for vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O

    # check for left-right diagonal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O

    # check for right-left diagonal
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check for winner
    if winner(board) is not None:
        return True

    # check for tie
    gameOver = True
    for row in board:
        for space in row:
            if space == EMPTY:
                gameOver = False

    return gameOver


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def maximizing(board, alpha, beta):
    """
    returns action that produces highest value from min value of results
    """
    action_list = actions(board)
    max_value = -math.inf
    optimal_action = None

    # loop through actions swapping turns
    for action in action_list:
        resulting_board = result(board, action)
        if terminal(resulting_board):
            value = utility(resulting_board)
            optimal_action = action
            return value, optimal_action
        else:
            value, act = minimizing(resulting_board, alpha, beta)
        if value > max_value:
            max_value = value
            alpha = max(alpha, max_value)
            optimal_action = action
        if beta <= alpha:
            break

    return max_value, optimal_action


def minimizing(board, alpha, beta):
    """
    returns action that produces lowest value from max value of results
    """
    action_list = actions(board)
    min_value = math.inf
    optimal_action = None

    # loop through actions swapping turns
    for action in action_list:
        resulting_board = result(board, action)
        if terminal(resulting_board):
            value = utility(resulting_board)
            optimal_action = action
            return value, optimal_action
        else:
            value, act = maximizing(resulting_board, alpha, beta)
        if value < min_value:
            min_value = value
            beta = min(beta, min_value)
            optimal_action = action
        if beta <= alpha:
            break

    return min_value, optimal_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        return maximizing(board, -math.inf, math.inf)[1]
    else:
        return minimizing(board, -math.inf, math.inf)[1]
