'''
주사위를 던지는 횟수(100이상)를 사용자가 입력
주사위를 던져서 주사위별 1,2,3,4,5,6이 각각 나올 확률


'''

import random

facelist =[0,0,0,0,0,0]
dice_num = 0
FACE_NUM = 6 # 주사위의 숫자는 6에서 끝남 무조건 사실 그냥 계산해도 될것 같음 

count = int(input("주사위를 던질 횟수를 입력하세요 (100이상)"))


if count< 100:
    print("100이상의 숫자를 입력하세요. 종료합니다.")
else:
    for i in range(count): #range() 마지막 숫자 빠짐 0~ n-1까지
        dice_num = random.randint(1,6) #randint는 마지막 숫자 포함 123456
        facelist[dice_num-1] = facelist[dice_num-1] + 1
    
for i in range(FACE_NUM):       
    print(f"주사위면 {i+1}: {facelist[i]}/{count}, 확률 : {round(facelist[i]/count, 2)}")


'''
여기서 알수 있는점
리스트는 순서를 가지고 저장
        여러개의 데이터 저장

'''

