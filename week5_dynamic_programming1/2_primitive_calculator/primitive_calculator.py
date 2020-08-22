# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    T = [0, 0] + [n] * (n-1)

    for i in range(2, n + 1):
        if T[i] > 1:
            T[i] = min(T[i], T[i - 1] + 1)
        if i % 2 == 0 and i / 2 >= 1:
            T[i] = min(T[i], T[int(i / 2)] + 1)
        if i % 3 == 0 and i / 3 >= 1:
            T[i] = min(T[i], T[int(i / 3)] + 1)

    result = [n] + [0] * T[n]

    for i in range(1, len(result)):
        if T[result[i - 1] - 1] == T[n] - i:
            result[i] = result[i - 1] - 1
        elif T[int(result[i - 1] / 2)] == T[n] - i:
            result[i] = int(result[i - 1]/ 2)
        else:
            result[i] = int(result[i - 1] / 3)

    return [ele for ele in reversed(result)]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

    
