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
    o_win = False
    x_win = False

    # check for horizontal win
    for row in board:
        if row[0] == row[1] == row[2] == X:
            x_win = True
            return X
        elif row[0] == row[1] == row[2] == O:
            o_win = True
            return O

    # check for vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            x_win = True
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            o_win = True
            return O

    # check for left-right diagonal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O

    # check for right-left diagonal
    if board [0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board [0][2] == board[1][1] == board[2][0] == O:
        return O

    # no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
