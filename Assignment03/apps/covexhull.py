# William Romine
# 00103649
# Dr. Lewis CS472
# https://stackoverflow.com/questions/62376042/calculating-and-displaying-a-convexhull

from typing import List, Tuple

Point = Tuple[int, int]

def cross_product(A: Point, B: Point, C: Point) -> int:
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def orientation(A: Point, B: Point, C: Point) -> int:
    cross = cross_product(A, B, C)
    if cross == 0:
        return 0
    return 1 if cross > 0 else -1

def convex_hull(points: List[Point]) -> List[Point]:
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

def print_points(points: List[Point]) -> None:
    for point in points:
        print(f"({point[0]}, {point[1]})", end=" ")
    print()

points = [(0, 6), (2, 2), (1, 1), (3, 7), (6, 0), (0, 0), (6, 6)]

print("Original Points:", end=" ")
print_points(points)

convex_hull_points = convex_hull(points)

print("Convex Hull Points:", end=" ")
print_points(convex_hull_points)
