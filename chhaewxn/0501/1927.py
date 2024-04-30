# heapq 모듈을 이용하자! 

import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):

    op = int(input())

    if op == 0:
        if not heap: # 힙이 비어있다면 0 출력
            print(0)
        else:
            print(heapq.heappop(heap)) # 힙에서 가장 작은 값을 출력하고 제거
    else: # 연산이 0이 아닌 경우 (정수 x를 추가하는 연산)
        # 힙에 정수 x를 추가
        heapq.heappush(heap, op)