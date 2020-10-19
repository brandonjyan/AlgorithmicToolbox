# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def compare(digit1, digit2):
    if int(str(digit1) + str(digit2)) > int(str(digit2) + str(digit1)):
        return digit1
    else:
        return digit2


def largest_number(numbers):
    answer = ""
    while len(numbers) > 0:
        maxDigit = 0
        for digit in numbers:
            maxDigit = compare(maxDigit, digit)
        numbers.remove(maxDigit)
        answer += str(maxDigit)
    return answer


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
