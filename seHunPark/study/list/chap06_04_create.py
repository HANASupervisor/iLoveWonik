'''
리스트 생성방법
'''

#1 초기값이 있는경우
scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

print(scores)

#2 빈 리스트 생성 후 데이터 추가
# append(데이터)
import random

scores = [] #or scores = list()

for i in range(10):
    #data = int(input("성적을 입력하시오 : "))
    data = random.randint(50,100)
    scores.append(data)

print(scores)
