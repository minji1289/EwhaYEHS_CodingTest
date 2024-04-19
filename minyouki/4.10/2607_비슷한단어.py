##구현
import sys
input = sys.stdin.readline

#입력
n = int(input())

#첫번째 단어 입력
first = list(input().rstrip())

#비슷한 단어 개수
ans = 0

#나머지 입력
for _ in range(1, n):
    word = list(input().rstrip())
    target = first[:] #첫 단어 복사

    len_diff = 0 #word와 target의 길이 차이
    for i in range(len(word)):
        if word[i] in target:
            target.remove(word[i])
        else:
            len_diff += 1

    if len(target) <= 1 and len_diff <= 1:
        ans += 1

print(ans)
