# William Romine
# 00103649
# Dr. Lewis CS472
# https://community.wolfram.com/groups/-/m/t/2983903
# https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072

import numpy as np
import networkx as nx

def sudoku_to_graph(puzzle):
    G = nx.Graph()
    for i in range(9):
        for j in range(9):
            G.add_node((i, j))
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if k != j:
                    G.add_edge((i, j), (i, k))
                if k != i:
                    G.add_edge((i, j), (k, j))
                if (i // 3 != k // 3) or (j // 3 != k % 3):
                    G.add_edge((i, j), (k // 3 + i // 3 * 3, k % 3 + j // 3 * 3))
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                for node in G.neighbors((i, j)):
                    G.remove_edge((i, j), node)
                G.nodes[(i, j)]['color'] = puzzle[i][j]
    return G

def graph_coloring(G):
    coloring = nx.coloring.greedy_color(G, strategy='largest_first')
    return coloring

def display_sudoku(puzzle):
    for row in puzzle:
        print(' '.join(map(str, row)))

def complete_sudoku(puzzle, coloring):
    completed_puzzle = np.copy(puzzle)
    for i in range(9):
        for j in range(9):
            if completed_puzzle[i][j] == 0:
                completed_puzzle[i][j] = coloring[(i, j)]
    return completed_puzzle

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

G = sudoku_to_graph(puzzle)
coloring = graph_coloring(G)
completed_puzzle = complete_sudoku(puzzle, coloring)

print("Original Sudoku puzzle:")
display_sudoku(puzzle)
print("\nCompleted Sudoku puzzle:")
display_sudoku(completed_puzzle)
