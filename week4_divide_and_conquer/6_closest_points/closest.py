# python3

from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared_wrapper(points):
    sorted_points = sorted(points, key=lambda p: p.x)
    return minimum_distance_squared(sorted_points)


def minimum_distance_squared(points):
    if len(points) <= 3:
        min_distance_squared = distance_squared(points[0], points[1])
        for p, q in combinations(points, 2):
            min_distance_squared = min(min_distance_squared,
                                       distance_squared(p, q))
        return min_distance_squared
    else:
        mid = len(points) // 2
        left_points = points[:mid]
        right_points = points[mid:]

        left_min = minimum_distance_squared(left_points)
        right_min = minimum_distance_squared(right_points)
        separated_min = min(left_min, right_min)

        strip = []
        midline = points[mid].x

        for point in left_points:
            if point.x > midline - separated_min:
                strip.append(point)

        for point in right_points:
            if point.x < midline + separated_min:
                strip.append(point)

        sorted_strip = sorted(strip, key=lambda p: p.y)

        combined_min = separated_min

        for i in range(len(sorted_strip)):
            for j in range(i + 1, min(i + 8, len(sorted_strip))):
                combined_min = min(combined_min, distance_squared(sorted_strip[i], sorted_strip[j]))

        return combined_min


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_wrapper(input_points))))

  
