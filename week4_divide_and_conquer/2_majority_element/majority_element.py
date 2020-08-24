# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element_internal(elements, left, right):
    assert len(elements) <= 10 ** 5

    if left + 1 == right:
        return elements[left]

    mid = (left + right - 1) // 2 + 1
    left_elem = majority_element_internal(elements, left, mid)
    right_elem = majority_element_internal(elements, mid, right)

    if left_elem == right_elem:
        return left_elem

    lcount = 0
    for i in range(left, right):
        if elements[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if elements[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


def majority_element(elements):
    if majority_element_internal(elements, 0, len(elements)) == -1:
        return 0
    else:
        return 1

    
if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

    
    
