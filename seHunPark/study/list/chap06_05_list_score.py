'''
리스트 요소(array element)
리스트에서 각 그릇에 0 ~ (리스트 크기 -1)
'''
scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

scores[0] = 80 # 인덱스 0번(32)를 80으로 변경
scores[1] = scores[0] # 인덱스 1번(56)을 인덱스 0번(80)으로 변경

print(scores) #80, 80, 변경X

i = 4
scores[i] = 10 #12가 바뀜
scores[i+2] = 20 # 수식이 인덱스가 된다.

print(scores)


number = 10

i = 5
if 0 <= i < len(scores):
    scores[i] = number

print(len(scores))