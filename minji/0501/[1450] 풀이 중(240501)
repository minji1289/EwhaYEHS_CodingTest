import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1) #dp[i]: i까지의 최대 이익

p_arr = []
t_arr = []

for i in range(n):
    t, p = map(int, input().split())
    p_arr.append(p)
    t_arr.append(t)
    
for i in range(n):
    #현재 있는 i를 선택할지말지..로 접근하자!
    if ((i+t_arr[i]) <= n):
        dp[i+t_arr[i]]=max(dp[i+t_arr[i]]+p_arr[i], dp[i+t_arr[i]])

print(dp[n])

##점화식 어렵당...
