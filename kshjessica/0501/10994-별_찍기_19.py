
"""
문제에서 유추하라고 제시한 규칙은 다음과 같다.

주어진 숫자 N에 따라 별 모양의 패턴을 생성하고 출력하는 것을 목표로 한다.

패턴은 크기가 4 * N - 3인 정사각형 모양으로 구성되고 패턴은 빈 공간으로 초기화된 2차원 리스트로 표현된다.

재귀 함수 fill_pattern을 사용하여 패턴을 채운다. 이 함수는 시작 좌표(x, y)와 패턴의 크기를 나타내는 숫자 n을 인자로 받는다.

재귀적으로 패턴을 채우는 방법은 다음과 같다:

1) 만약 n이 1이라면,
패턴의 시작 좌표에 '*'을 채운다.
2) 그렇지 않다면,
외부 사각형과 내부 사각형을 채운다.
- 외부 사각형은 시작 좌표(x, y)를 기준으로 4 * n - 3만큼의 길이를 가지며, 모서리와 변에 '*'을 채운다.
- 내부 사각형은 시작 좌표(x + 2, y + 2)와 크기 n - 1을 인자로 하여 fill_pattern 함수를 재귀적으로 호출한다.
"""

N = int(input())

# Calculate the size of the pattern
size = 4 * N - 3

# Create the pattern
pattern = [[' '] * size for _ in range(size)]

# Recursive function to fill the pattern
def fill_pattern(x, y, n):
    if n == 1:
        pattern[x][y] = '*'
        return

    # Fill the outer square
    for i in range(x, x + 4 * n - 3):
        pattern[x][i] = '*'
        pattern[x + 4 * n - 4][i] = '*'
        pattern[i][y] = '*'
        pattern[i][y + 4 * n - 4] = '*'

    # Fill the inner square
    fill_pattern(x + 2, y + 2, n - 1)

# Fill the pattern recursively
fill_pattern(0, 0, N)

# Print the pattern
for row in pattern:
    print(''.join(row))