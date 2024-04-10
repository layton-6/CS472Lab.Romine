# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/sudoku-backtracking-7/
# https://levelup.gitconnected.com/sudoku-solver-python-using-backtracking-1aff17a3340

def is_valid(grid, row, col, num):
    for x in range(9):
        if (grid[row][x] == num or grid[x][col] == num):
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if (grid[i + start_row][j + start_col] == num):
                return False

    return True

def slv_sudoku(grid, n):
    for row in range(n):
        for col in range(n):

            if (grid[row][col] == 0):
                for num in range(1, 10):

                    if (is_valid(grid, row, col, num)):
                        grid[row][col] = num

                        if (slv_sudoku(grid, n)):
                            return True

                        grid[row][col] = 0

                return False

    return True

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

def puzz_frm_file(filename):
    with open(filename, "r") as file:
        puzzle = [[int(cell) for cell in line.strip().split()] for line in file.readlines()]
    return puzzle

def wrt_soln_file(filename, solution):
    with open(filename, "w") as file:
        for row in solution:
            for cell in row:
                file.write(f"{cell} ")
            file.write("\n")

def main():
    filename = "puzzle.txt"
    puzzle = puzz_frm_file(filename)

    if (slv_sudoku(puzzle, 9)):
        print_grid(puzzle)
        wrt_soln_file("solution.txt", puzzle)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()