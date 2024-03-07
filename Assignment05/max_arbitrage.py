# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

import networkx as nx

def max_arbitrage(R):
    n = len(R)
    max_profit = 0
    max_cycle = []

    S = nx.zeros((n, n))
    for i in range(n):
        for j in range(n):
            S[i][j] = R[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][k] + S[k][j] > S[i][j]:
                    S[i][j] = S[i][k] + S[k][j]
                    if i == j:
                        max_profit = max(max_profit, S[i][j])
                        max_cycle = [i]
                    elif S[i][j] > 1:
                        max_profit = max(max_profit, S[i][j])
                        max_cycle = [i, j]

    if max_profit > 1:
        i = 0
        while i < len(max_cycle) - 1:
            j = (i + 1) % len(max_cycle)
            k = (i + 2) % len(max_cycle)
            if S[max_cycle[i]][max_cycle[j]] + S[max_cycle[j]][max_cycle[k]] > S[max_cycle[i]][max_cycle[k]]:
                max_cycle.insert(i + 1, max_cycle[j])
            i += 1

    return max_profit, max_cycle