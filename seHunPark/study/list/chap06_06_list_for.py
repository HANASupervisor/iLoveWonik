temps = [28, 31, 33, 35, 27, 26, 25]

#리스트 순회 방법 1: 인덱스 및 리스트의 길이(len(리스트)) 사용
for i in range(len(temps)): # range를 7번 반복
    print(temps[i], end='') # temps[i]    i <= 0123456 
print()

#리스트 순회 방법 2: 단순히 값을 가져옴
for element in temps:
    print(element, end = '')
print()

for i in temps:
    print(i)
print()