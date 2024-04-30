import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    days = int(input()) #전체 날 수
    price = list(map(int, input().split())) #날 별 주식 가격

    #앞에서부터 탐색 시, max 함수 이용해 최대값 찾아야 하므로 시간 초과 발생
    #현재 인덱스(i)의 값을 최대값으로 두고 일렬로만 탐색하기 위해 리스트를 뒤집음
    price.reverse()

    profit = 0 #최대 이익
    i = 0 #현 위치 인덱스
    while True:
        j = i+1 #다음 최대값까지 이동시킬 인덱스
        while j < days and price[i] > price[j]: #다음 최대값까지 이동
            j += 1
        profit += price[i] * (j-i) - sum(price[i:j])
        i = j #다음 최대값부터 다시 탐색하기 위해 준비
        if j >= days:
            break
    print(profit)
