# 21921번 - 블로그 
import sys

input = sys.stdin.readline

n,x = map(int, input.split())
visitor = list(map(int, input.split()))

# x 기간 동안 총 방문자 수 합 계산 
max_sum = sum(visitor[:x])
now_sum = max_sum
count = 1

for i in range(x, n):
  now_sum = now_sum - visitor[i-x] + visitor[i] # 오래된 날짜의 방문자 수는 빼고, 새로운 날짜 추가하기

  if now_sum > max_sum :
    max_sum = now_sum
    count = 1 # 최대 방문자 수 갱신
  elif now_sum == max_sum :
    count += 1 # 최대 방문자 수가 동일하면 count +1 추가

if max_sum == 0:
  print("SAD")
else:
  print(max_sum)
  print(count)