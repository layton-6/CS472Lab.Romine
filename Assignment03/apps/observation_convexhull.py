# William Romine
# 00103649
# Dr. Lewis CS472
# https://www.geeksforgeeks.org/python-generate-random-numbers-within-a-given-range-and-store-in-a-list/

from typing import List, Tuple

def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

    def cross_product(A: Tuple[int, int], B: Tuple[int, int], C: Tuple[int, int]) -> int:
        return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

    def orientation(A: Tuple[int, int], B: Tuple[int, int], C: Tuple[int, int]) -> int:
        cross = cross_product(A, B, C)
        if cross == 0:
            return 0
        return 1 if cross > 0 else -1

    n = len(points)
    if n <= 3:
        return points

    points.sort()

    hull = []

    left, right = [], []
    for i in range(n):
        while len(left) >= 2 and orientation(left[-2], left[-1], points[i]) != -1:
            left.pop()
        left.append(points[i])
    for i in range(n - 1, -1, -1):
        while len(right) >= 2 and orientation(right[-2], right[-1], points[i]) != -1:
            right.pop()
        right.append(points[i])

    for p in left:
        hull.append(p)
    for p in right[1:-1]:
        hull.append(p)

    return hull

def read_observations(filename: str) -> List[Tuple[int, int]]:
    observations = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            observations.append((x, y))
    return observations

def generate_random_observations(filename: str, num_points: int):
    import random
    with open(filename, 'w') as file:
        for _ in range(num_points):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            file.write(f"{x} {y}\n")

def print_points(points: List[Tuple[int, int]]):
    for point in points:
        print(f"({point[0]}, {point[1]})", end=" ")
    print()

def main():
    generate_random_observations("observations.txt", 100) 

    observations = read_observations("observations.txt")

    convex_hull_points = convex_hull(observations)

    print("Convex hull points:")
    print_points(convex_hull_points)

if __name__ == "__main__":
    main()
