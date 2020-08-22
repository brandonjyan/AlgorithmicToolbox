# python3

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    arr = [[[0 for _ in range(len(third_sequence) + 1)] for _ in range(len(second_sequence) + 1)] for _ in range(len(first_sequence) + 1)]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            for k in range(1, len(third_sequence) + 1):
                diff = 1 if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1] else 0
                arr[i][j][k] = max(arr[i - 1][j][k], arr[i][j - 1][k], arr[i][j][k - 1], arr[i - 1][j - 1][k - 1] + diff)

    return arr[len(first_sequence)][len(second_sequence)][len(third_sequence)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

