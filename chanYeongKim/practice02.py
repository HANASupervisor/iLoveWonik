"""
클래스/예외처리 실습_오후
260706
김찬영
"""

#상속 실습_오버라이딩
# #부모 클래스 선언
# class Car:
#     speed = 0
#     def up_speed(self, value):
#         self.speed += value
#         print(f'현재 속도(슈퍼 클래스): {self.speed}')
#
# #자녀 클래스 선언
# class Sedan(Car):
#     def up_speed(self, value):
#         self.speed += value
#         if self.speed > 150:
#             self.speed = 150 #속도 150 넘어갈시 최대 속도 150으로 제한
#         print(f'현재 속도(서브 클래스): {self.speed}') #속도 출력
#
# class Truck(Car):
#     pass #부모 클래스 편집 없이 그대로 사용
#
# #변수 선언
# sedan1 = None
# truck1 = None
#
# #메인 코드 부분
# sedan1 = Sedan()
# truck1 = Truck()
#
# print('트럭 -->', end='')
# truck1.up_speed(200)
#
# print('승용차-->', end='')
# sedan1.up_speed(200)

#try/except 실습
# try :
#     print(x)
# except :
#     print('Error')

# print(x)

# try:
#     print(10/0)
# except NameError:
#     print('Variable x is not defined')
# except:
#     print('Something else went wrong')

#try/except 응용: 계산기
while True:
    try:
        num1 = int(input('첫 번째 숫자를 입력하세요: '))
        num2 = int(input('두 번째 숫자를 입력하세요: '))

        result = num1 / num2
        print(f'계산 결과: {result}')
        break #계산이 정상적으로 이루어지면 반복문 종료

    except ValueError:
        print('숫자만 입력하세요. 다시 입력합니다.\n')

    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다. 다시 입력합니다.\n')