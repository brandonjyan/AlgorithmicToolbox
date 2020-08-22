# python3

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    arr = [[0 for _ in range(len(second_sequence) + 1)] for _ in range(len(first_sequence) + 1)]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            diff = 1 if first_sequence[i - 1] == second_sequence[j - 1] else 0
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1] + diff)

    return arr[len(first_sequence)][len(second_sequence)]


if __name__ == '__main__':
    # print(lcs2([7, 2, 9, 3, 1, 5, 9, 4], [2, 8, 1, 3, 9, 7]))

    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

    
