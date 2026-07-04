'''
주사위를 던지는 횟수(100이상)를 사용자가 입력
주사위를 던져서 주사위별 1,2,3,4,5,6이 각각 나올 확률
'''
import random

count = int(input("주사위 던질 횟수를 입력하세요! :"))

flag = True
while flag:
    if count < 100:
        pass
    