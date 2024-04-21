import sys
input = sys.stdin.readline

#입력
n = int(input())
D = list(map(int, input().split()))
P = list(map(int, input().split()))

#시간초과
# total_p = d[0] * p[0]
# s = 0
# for e in range(1, len(d)):
#     min_p = min(p[s:e+1])
#     total_p += min_p * d[e]
#     if min_p == p[e]:
#         s = e
cost = P[0]
total_cost = 0
for i in range(n-1):
    if cost > P[i]:
        cost = P[i]
    total_cost += D[i] * cost

print(total_cost)
