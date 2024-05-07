import sys

input = sys.stdin.readline

n = int(input())  # 탑의 개수 입력 받기
tops = list(map(int, input().split()))  # 각 탑의 높이 입력 받기
stack = []  # 스택 초기화
answer = [0] * n  # 각 탑의 신호를 수신하는 탑의 위치를 저장할 리스트

for i in range(n):
    while stack and stack[-1][0] < tops[i]:  # 현재 탑의 높이가 스택의 마지막 탑 높이보다 클 때
        stack.pop()  # 스택에서 탑을 제거
    if stack:  # 스택이 비어있지 않다면, 현재 탑의 신호를 수신할 탑이 스택에 있음
        answer[i] = stack[-1][1] + 1  # 인덱스는 0부터 시작하므로, 1을 더해줌
    stack.append((tops[i], i))  # 현재 탑을 스택에 추가 (탑의 높이, 인덱스)

print(' '.join(map(str, answer)))  # 결과 출력
