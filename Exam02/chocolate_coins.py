# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/dynamic-programming-dp-on-arrays-tutorial/

def max_coins(C):
    n, m = len(C), len(C[0])
    F = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        F[0][j] = C[0][j]

    for i in range(n):
        F[i][0] = C[i][0]

    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = max(F[i-1][j], F[i][j-1]) + C[i][j]

    max_coins_count = F[n-1][m-1] + F[0][0]

    print(f"The total chocolate coins the robotic Oompa-Loompa can pick up is: {max_coins_count}")

# Sample layout of chocolate coins
C = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1]
]

max_coins(C)
