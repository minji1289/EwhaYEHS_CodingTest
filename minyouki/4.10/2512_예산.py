import sys
input = sys.stdin.readline

#입력
n = int(input())
budget = list(map(int, input().split()))
total_budget = int(input())

low, high = 0, max(budget)

if sum(budget) <= total_budget: #모든 요청이 배정될 수 있는 경우
    print(max(budget))
else: #모든 요청이 배정될 수 없는 경우
    while(low <= high):
        mid = (low + high) // 2
        sum_budget = sum([min(mid, k) for k in budget])

        if sum_budget <= total_budget:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)
