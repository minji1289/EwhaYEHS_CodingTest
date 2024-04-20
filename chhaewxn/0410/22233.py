import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
keywords = set(sys.stdin.readline().rstrip() for _ in range(n))

for _ in range(m):
    # 공백으로 구분된 키워드를 한 번에 제거하기 위해 입력 받은 문자열을 집합으로 변환
    to_remove = set(sys.stdin.readline().rstrip().split(','))
    # 교집합을 이용해 한 번에 제거
    keywords -= to_remove
    print(len(keywords))
