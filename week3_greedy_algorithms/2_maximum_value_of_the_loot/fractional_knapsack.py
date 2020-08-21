# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    price_per_weight = [int(p) / int(w) for p, w in zip(prices, weights)]
    value = 0

    while capacity > 0 and max(price_per_weight) != -1:
        index = price_per_weight.index(max(price_per_weight))

        if weights[index] > capacity:
            value += price_per_weight[index] * capacity
        else:
            value += prices[index]

        capacity -= weights[index]
        price_per_weight[index] = -1

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


    
