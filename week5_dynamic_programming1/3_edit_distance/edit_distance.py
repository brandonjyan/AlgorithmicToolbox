# python3

def edit_distance(first_string, second_string):
    arr = [[0 for _ in range(len(second_string) + 1)] for _ in range(len(first_string) + 1)]

    for i in range(1, len(first_string) + 1):
        arr[i][0] = i

    for i in range(1, len(second_string) + 1):
        arr[0][i] = i

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            diff = 0 if first_string[i - 1] == second_string[j - 1] else 1
            arr[i][j] = min(arr[i - 1][j] + 1, arr[i][j - 1] + 1, arr[i - 1][j - 1] + diff)


    return arr[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

   
