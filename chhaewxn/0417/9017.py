# 9017. 크로스 컨트리
# 팀 인원이 6명 미만이면, 점수 계산에서 제외시킴
# 동일한 점수일 때, 5번째 선수의 점수가 적은 팀이 우승함 
import sys

input = int(sys.stdin.readline().strip())

for _ in range(input):
  n = int(sys.stdin.readline().strip())
  rank = list(map(int, sys.stdin.readline().split()))
  result = {}

  for data in rank:
    result[data] = result.get(data, 0) + 1

  fifth_score = [0] * (max(result.keys()) + 1) # 5번째 선수의 점수 저장하는 배열 
  score_map = {} # 팀의 총 점수 저장
  score = 1
  temp = {} # 팀별로 처리된 선수의 수를 임시로 저장

  for element in rank:
    if result[element] >= 6:
      temp[element] = temp.get(element, 0) + 1

      if temp[element] <= 4:
        score_map[element] = score_map.get(element, 0) + score

      if temp[element] == 5:
        fifth_score[element] = score
      score += 1
      
  key_data = list(score_map.keys())
  key_data.sort(key=lambda x: (score_map[x], fifth_score[x]))
  print(key_data[0])