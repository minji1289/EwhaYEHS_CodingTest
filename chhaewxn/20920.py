# 길이가 목표 길이와 같은 단어들을 최소 출현 빈도가 높은 순으로 정렬
# 출현 빈도가 동일한 경우, 길이가 더 긴 단어가 앞에 위치
# 길이가 목표 길이와 같고, 출현 빈도도 동일한 경우, 사전 순으로 정렬

import sys

# 입력 받기 - 맨 끝의 \n까지 같이 입력받기 때문에 rstrip()을 추가
n, m = map(int, input().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

# 단어의 길이와 단어가 나온 횟수를 저장할 딕셔너리(key-value) 생성
word_counts = {}

# 각 단어의 길이와 횟수를 계산하여 딕셔너리에 저장
for word in words:
    if len(word) >= m:
        word_counts[word] = word_counts.get(word, 0) + 1

# 정렬 기준에 맞게 정렬 (횟수 내림차순, 길이 내림차순, 사전 순)
sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for word, count in sorted_words:
    print(word)