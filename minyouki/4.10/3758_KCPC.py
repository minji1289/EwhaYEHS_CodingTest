import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
    n, k, t, m = map(int, input().split())
    score = [[0] * (k+2) for _ in range(n+1)] #idx=k+1에 점수 총합 저장
    submit = [[i, 0, 0] for i in range(n+1)] #idx=0에 팀 번호, idx=1에 제출횟수, idx=2에 마지막 제출시간

    for time in range(m):
        # 팀 ID i, 문제 번호 j, 획득한 점수 s
        i, j, s = map(int, input().split())
        if score[i][j] < s:
            score[i][j] = s
        submit[i][1] += 1
        submit[i][2] = time

    for s in score:
        s[k+1] = sum(s[:k+1])

    submit.sort(key = lambda x : (-score[x[0]][k+1], x[1], x[2]))

    print([idx+1 for idx, sub in enumerate(submit) if sub[0] == t][0])
