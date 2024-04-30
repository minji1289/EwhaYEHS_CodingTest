# 2512번 예산
# 총 예산이 최대 한도(M)를 초과하지 않는 경우는 예산을 늘려도 된다
# 총 예산이 최대 한도(M)를 초과하는 경우는 예산을 줄여야 한다

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