# 2607 - 비슷한 단어
# 두 문자열의 길이 차이가 1 이하 
# 두 문자열을 구성하는 문자의 종류 차이가 1 이하

from collections import Counter

n = int(input())
original_word = input()
words = [input() for _ in range(n-1)]

original_word_len = len(original_word)
original_word_count = Counter(original_word)

similar_count = 0

for word in words:
    if abs(len(word) - original_word_len) > 1:
        continue

    word_count = Counter(word)
    diff_count = sum((original_word_count - word_count).values())

    if diff_count <= 1:
        similar_count += 1

print(similar_count)