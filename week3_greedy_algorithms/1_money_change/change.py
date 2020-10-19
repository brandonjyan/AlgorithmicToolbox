# python3

def money_change(money):
    assert 0 <= money <= 10 ** 3
    counter = 0

    if money >= 10:
        counter += money // 10
        money %= 10
    if money >= 5:
        counter += money // 5
        money %= 5

    return counter + money

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
