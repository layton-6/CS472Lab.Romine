# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/
# https://www.geeksforgeeks.org/decrease-and-conquer/

def arr_tiles(n, board):
    def is_val(board):
        for i in range(n):
            if board[i][n - 1] == board[i][n - 2] or board[i][n - 2] == board[i][n - 3]:
                return False
        return True

    def helper(board, start):
        if start == n:
            return is_val(board)

        for i in range(start, n):
            board[i], board[start] = board[start], board[i]
            if helper(board, start + 1):
                return True
            board[i], board[start] = board[start], board[i]

        return False

    return helper(board, 0)

n = 3
board = [['R', 'W', 'B', 'R', 'W', 'B','R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B','R', 'W', 'B'],
          ['W', 'B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B'],
          ['B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B', 'R', 'W', 'B']]

result = arr_tiles(n, board)
if result:
    print("Tiles arranged successfully!")
else:
    print("Impossible to arrange tiles successfully!")