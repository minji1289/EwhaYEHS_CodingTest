T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    money = 0
    max_price = 0

    for i in range(len(prices)-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            money += max_price - prices[i]

    print(money)
