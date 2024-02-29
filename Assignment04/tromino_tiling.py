# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/domino-and-tromino-tiling-problem/

import math

def is_power_of_two(n):
    return n and (not (n & (n - 1)))

def is_valid_position(board, x, y, tromino):
    if x < 0 or y < 0 or x + len(tromino) > len(board) or y + len(tromino[0]) > len(board):
        return False
    for i in range(len(tromino)):
        for j in range(len(tromino[0])):
            if tromino[i][j] == 1 and board[x + i][y + j] == 1:
                return False
    return True

def find_forbidden_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1:
                return i, j
    return None

def solve_tiling_problem(board):
    tromino_i = [[0, 0, 1], [1, 0, 0], [0, 1, 1]]
    tromino_l = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    trominos = [tromino_i, tromino_l]
    forbidden_square = find_forbidden_square(board)
    if forbidden_square is None:
        return None
    n = len(board)
    if not is_power_of_two(n):
        return None
    x, y = forbidden_square
    tromino_count = 0
    for tromino in trominos:
        if is_valid_position(board, x, y, tromino):
            for i in range(len(tromino)):
                for j in range(len(tromino[0])):
                    board[x + i][y + j] = tromino[i][j]
            tromino_count += 1
            if tromino_count == 2:
                return board
            for i in range(len(tromino)):
                for j in range(len(tromino[0])):
                    board[x + i][y + j] = 0
    # If no solution is found, add a tromino to the top-left corner
    if is_valid_position(board, 0, 0, tromino_i):
        for i in range(len(tromino_i)):
            for j in range(len(tromino_i[0])):
                board[i][j] = tromino_i[i][j]
        return board
    else:
        return None

def main():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    forbidden_square = (0, 0)
    board[forbidden_square[0]][forbidden_square[1]] = -1
    solution = solve_tiling_problem(board)
    if solution is not None:
        for row in solution:
            print(row)

if __name__ == "__main__":
    main()
