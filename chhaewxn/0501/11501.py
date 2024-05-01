# 11501 주식
# 뒤에서부터 앞으로 역순으로 가며 가장 큰 값을 갱신하면서, 이 값과의 차이를 계산하기!

import sys

input = sys.stdin.readline

T = int(input()) # T: 테스트케이스 개수

for _ in range(T):
    
    n = int(input())
    prices = list(map(int, input().split()))
    
    max_profit = 0
    max_price = 0 # 현재 최대 주식 가격
    
    # 뒤에서부터 주식 가격을 확인
    for i in range(n-1, -1, -1):
        # 현재 확인하고 있는 가격
        current_price = prices[i]
        # 현재 가격이 현재까지의 최대 가격보다 큰 경우, 최대 가격을 현재 가격으로 갱신
        if current_price > max_price:
            max_price = current_price
        # 현재 가격이 최대 가격보다 작은 경우, 이 차이만큼이 이익이므로 더하기
        else:
            max_profit += max_price - current_price
    
    print(max_profit)
