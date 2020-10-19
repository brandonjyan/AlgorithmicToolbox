# python3

from collections import namedtuple
from sys import stdin
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    points = []

    segments.sort(key=attrgetter("end"))
    max_right = segments[0].end
    points.append(max_right)

    i = 1
    while i < len(segments):
        if max_right < segments[i].start:
            max_right = segments[i].end
            points.append(max_right)
        i += 1

    return points

if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
