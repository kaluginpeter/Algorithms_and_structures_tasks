# You work as a data scientist at an IT company, and your boss, all of a sudden, asked you to find the most common patterns in Tic Tac Toe games submitted to a survey on your company's website.
#
# However, some of them are not from real games, i. e. the position on such a game board cannot be reached through normal play.
#
# You have to find a way to filter out such "games", leaving only the correct (reachable) ones.
#
# Task
# You will be given a 3x3 array of character arrays (tuple of string tuples in Python, or array of strings in JS; see example tests for your language) representing a Tic Tac Toe game board, with the following specifications:
#
# 'X' is a square occupied by player X,
# 'O' is a square occupied by player O,
# '_' is a square not occupied by either player.
# Given this board, you need to determine whether this board represents a position that is reachable through normal play, and return a boolean value: true (if the condition is satisfied) and false otherwise.
#
# Validation rules:
#
# 'X' should always be the first player to move.
# During one move, a player must occupy one extra square.
# If a player manages to occupy 3 squares in a row (horizontally, vertically or diagonally), the game is immediately over and no further moves can be made; that player wins and is declared victorious (such a game is valid).
# If all squares are occupied and neither player managed to get 3 in a row, the game ends in a draw (which is valid).
# Games where not all squares are occupied and neither player got 3 in a row are considered valid.
# Special case: This board (and similar ones where 'X' has two three-in-a-rows but the position can be reached):
#
# X X X
# O O X
# O O X
# should result in true.
#
# The board is guaranteed to be 3x3 and to consist of only 'X', 'O' or '_'.
#
# Good luck!
#
# ArraysAlgorithmsGamesLogic
# Solution
def is_win(board: tuple[tuple[str]], target: str) -> bool:
    # horizontal
    if any(row.count(target) == 3 for row in board): return True
    # vertical
    if any([board[j][i] for j in range(3)].count(target) == 3 for i in range(3)): return True
    # diagonal
    if [board[i][i] for i in range(3)].count(target) == 3 or [board[i][-i - 1] for i in range(3)].count(target) == 3: return True
    return False

def get_count(board: tuple[tuple[str]], target: str) -> int:
    return sum(row.count(target)for row in board)

def is_valid_position(board: tuple[tuple[str]]) -> bool:
    if is_win(board, 'X') and is_win(board, 'O'): return False
    elif is_win(board, 'X') and get_count(board, 'X') - get_count(board, 'O') != 1: return False
    elif is_win(board, 'O') and get_count(board, 'X') != get_count(board, 'O'): return False
    elif get_count(board, 'O') - get_count(board, 'X') > 0: return False
    elif get_count(board, 'X') - get_count(board, 'O') > 1: return False
    return True