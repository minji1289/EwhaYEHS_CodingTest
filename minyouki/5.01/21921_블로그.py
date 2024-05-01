import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))

sum_visit = sum(visit[0:x])
max_count = 1
max_visit = sum_visit

for i in range(1, n-x+1):
    sum_visit = sum_visit - visit[i-1] + visit[i+x-1]

    if sum_visit > max_visit:
        max_visit = sum_visit
        max_count = 1
    elif sum_visit == max_visit:
        max_count += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(max_count)
