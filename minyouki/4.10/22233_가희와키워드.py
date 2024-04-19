import sys
input = sys.stdin.readline

#입력
n, m = map(int, input().split())

keyword = dict()
for _ in range(n):
    keyword[input().rstrip()] = 1
ans = len(keyword)

for i in range(m):
    posting = list(input().rstrip().split(','))
    for p in posting:
        if p in keyword.keys():
            if keyword[p] == 1:
                keyword[p] -= 1
                ans -= 1
    print(ans)

