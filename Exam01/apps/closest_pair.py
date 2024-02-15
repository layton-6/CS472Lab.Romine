# William Romine
# 00103649
# Dr. Lewis CS472
# https://codereview.stackexchange.com/questions/28207/finding-the-closest-point-to-a-list-of-points

import math

def closest_pair(pairs, dist_funct):
    def euclidian_dist(p1, p2):
        return sum((x - y) ** 2 for x, y in zip(p1, p2))

    def hamming_dist(p1, p2):
        return sum(x != y for x, y in zip(p1, p2))

    def brute_force(pairs):
        min_distance = float('inf')
        closest_pair = None
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                distance = dist_funct(pairs[i], pairs[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (pairs[i], pairs[j])
        return closest_pair, min_distance

    def closest_pair_recursive(pairs):  
        if len(pairs) <= 3:
            return brute_force(pairs)

        mid = len(pairs) // 2
        mid_point = pairs[mid][0]

        left_pairs = [pair for pair in pairs if pair[0] < mid_point]
        right_pairs = [pair for pair in pairs if pair[0] >= mid_point]

        closest_pair_left, min_distance_left = closest_pair_recursive(left_pairs) 
        closest_pair_right, min_distance_right = closest_pair_recursive(right_pairs)  

        min_distance = min(min_distance_left, min_distance_right)
        closest_pair = closest_pair_left if min_distance == min_distance_left else closest_pair_right

        strip = [pair for pair in pairs if abs(pair[0] - mid_point) < min_distance]
        strip.sort(key=lambda pair: pair[1])

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                distance = dist_funct(strip[i], strip[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (strip[i], strip[j])

        return closest_pair, min_distance

    if dist_funct == 'euclidean':
        dist_funct = euclidian_dist
    elif dist_funct == 'hamming':
        dist_funct = hamming_dist

    if len(pairs) <= 3:
        return brute_force(pairs)
    else:
        return closest_pair_recursive(sorted(pairs)) 

pairs = [(1, 2), (3, 7), (4, 9), (8, 8), (10, 4)]
closest_pair, min_distance = closest_pair(pairs, 'euclidean')
print(f'Closest Pair: {closest_pair}')
print(f'Minimum Distance: {math.sqrt(min_distance)}')
