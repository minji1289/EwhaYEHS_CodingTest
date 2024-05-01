# 선택거리 K 이하의 왼쪽에 위치한 햄버거 먹기 
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 테이블 크기는 N, 선택 거리는 K 이하
string = input().rstrip() # P,H로 이루어진 길이가 N인 문자열
table_list = list(string)
count = 0

for i in range(len(table_list)):
  if table_list[i] == "P":
    for j in range(i-K, i+K+1): # 왼쪽으로 선택 거리 K 이내의 햄버거 확인하기
      if 0 <= j < N and table_list[j] == "H": # 인덱스가 테이블 범위 내에 있고, 햄버거가 있는 경우
        count += 1
        table_list[j] = "E" # 먹은 햄버거 
        break

print(count)
