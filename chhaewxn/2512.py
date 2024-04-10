n = int(input())
budget = list(map(int, input().split()))
m = int(input())

low, high = 0, max(budget)
answer = 0

if sum(budget) <= m:
    print(high)
else:
    while low <= high:
        mid = (low + high) // 2

        total_budget = sum(min(mid, b) for b in budget)

        if total_budget <= m:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)