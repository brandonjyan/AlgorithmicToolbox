# python3

from itertools import chain
from sys import stdin
from bisect import bisect_left, bisect_right

def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    result = [0] * len(points)
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    point_points = zip(points, ['p'] * len(points), range(len(points)))

    combined_list = chain(start_points, end_points, point_points)
    combined_list = sorted(combined_list, key=lambda a: (a[0], a[1]))

    counter = 0
    for point, type, index in combined_list:
        if type == 'l':
            counter += 1
        elif type == 'r':
            counter -= 1
        else:
            result[index] = counter

    return result


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
    
    
    
