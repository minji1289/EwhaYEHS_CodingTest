# 두 문자열의 길이 차이가 1 이하 
# 두 문자열을 구성하는 문자의 종류 차이가 1 이하

n = int(input()) # 단어의 개수 입력받기
word = input() # 첫 번째 단어 입력받기
similar_word_list = [input() for _ in range(n-1)] # 비슷한 단어 리스트 입력받기 
similar_word_count = 0

for similar_word in similar_word_list:
  if abs(len(word) - len(similar_word)) <= 1 and sum(1 for char in set(word) if char not in similar_word) <= 1:
      similar_word_count += 1

print(similar_word_count) 