# python3

def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    return fibonacci_number(n % period_length(m)) % m

def fibonacci_number(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current

def period_length(m):
    assert 2 <= m <= 10 ** 3

    previous = current = -1
    counter = 0
    while previous != 0 or current != 1:
        previous, current = current, (fibonacci_number(counter + 2) % m)
        counter += 1

    return counter

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
    
    
