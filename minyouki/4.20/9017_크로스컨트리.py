#구현
import sys
input = sys.stdin.readline

from collections import Counter

#입력
t = int(input())

for _ in range(t):
    n = int(input())
    teams = list(map(int, input().split()))

    #실격 팀 (딕셔너리)
    n_a = {key:value for key, value in dict(Counter(teams)).items() if value == 6}

    #팀별 점수 저장 - 각 인덱스가 팀 번호
    team_score = [[] for _ in range(201)] #201행 짜리 이차원 배열
    cnt = 1
    for i in range(len(teams)):
        if teams[i] in n_a:
            team_score[teams[i]].append(cnt)
            cnt += 1

    #팀별 1~4등 점수 합 저장
    team_total = [0] * 201
    for i in range(201):
        if i not in n_a:
            team_total[i] = 10000
        else:
            team_total[i] = sum(team_score[i][:4])

    #1등 팀 구하기
    min_score = min(team_total)
    if team_total.count(min_score) == 1: #1등이 하나
        print(team_total.index(min_score))
    else:
        min_five = 1000
        min_idx = 0
        for i in range(1, 201):
            if team_total[i] == min_score and min_five > team_score[i][4]:
                min_five = team_score[i][4]
                min_idx = i
        print(min_idx)

