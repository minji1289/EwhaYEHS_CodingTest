import sys
input = sys.stdin.readline

#입력
n, m = map(int, input().split())

word_dict = {} #word내용-word빈도
for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

#정렬
sorted_word = sorted(word_dict.keys(), key=lambda x: (-word_dict[x], -len(x), x))

#출력
for word in sorted_word:
    print(word)
