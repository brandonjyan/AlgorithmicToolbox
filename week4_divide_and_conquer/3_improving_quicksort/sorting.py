# python3

from random import randint

def partition3(array, left, right):
    x = array[left]
    j = k = left

    for i in range(left + 1, right + 1):
        if array[i] == x:
            j += 1
            array[i], array[j] = array[j], array[i]
        elif array[i] < x:
            j += 1
            k += 1
            array[i], array[j] = array[j], array[i]
            array[j], array[k] = array[k], array[j]

    array[left], array[k] = array[k], array[left]

    return [k, j]


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    #make a call to partition3 and then two recursive calls to randomized_quick_sort
    partitions = partition3(array, left, right)

    randomized_quick_sort(array, left, partitions[0] - 1)
    randomized_quick_sort(array, partitions[1] + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

    
    
