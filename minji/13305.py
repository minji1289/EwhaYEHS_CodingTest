import sys

input = sys.stdin.readline
n = int(input())

distance=list(map(int, input().split(" "))) #n-1개
cost=list(map(int, input().split(" "))) #n개

price = cost[0]
result = 0

for i in range(0, n-1):
	if (price <= cost[i+1]):
		result += (price * distance[i])
	elif price > cost[i+1]:
		result += (price*distance[i])
		price = cost[i+1] #다음 도시의 cost가 더 싸면 price 바꾸기!

print(result)
