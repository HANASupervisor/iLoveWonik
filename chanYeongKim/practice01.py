"""
클래스 실습_오전
260706
김찬영
"""

#11-02

# #클래스 정의 부분
# class Car:
#     #속성 부여
#     color = '' #색상
#     speed = 0  #속도
#
#     #메서드 부여
#     def up_speed(self, value):
#         self.speed += value #속도 증가
#
#     def down_speed(self, value):
#         self.speed -= value #속도 감소
#
# #객체 형성
# my_car1 = Car() #자동차1 객체 형성
# my_car2 = Car() #자동차2 객체 형성
# my_car3 = Car() #자동차3 객체 형성
#
# #메인 코드 부분
# my_car1.color = '빨강' #자동차1 색상 부여
# my_car2.color = '파랑' #자동차2 색상 부여
# my_car3.color = '노랑' #자동차3 색상 부여
#
# my_car1.speed = 10 # 자동차1 속도 부여
# my_car2.speed = 20 #자동차2 속도 부여
# my_car3.speed = 30 #자동차3 속도 부여
#
# #출력
# print(f'자동차1의 색상은 {my_car1.color}이며, 현재속도는 {my_car1.speed}km/h 입니다.')
# print(f'자동차2의 색상은 {my_car2.color}이며, 현재속도는 {my_car2.speed}km/h 입니다.')
# print(f'자동차3의 색상은 {my_car3.color}이며, 현재속도는 {my_car3.speed}km/h 입니다.')
#
# #메소드 실행
# my_car1.up_speed(30) #속도 30 증가
# my_car2.up_speed(30) #속도 30 증가
# my_car3.up_speed(30) #속도 30 증가
#
# #출력
# print(f'자동차1의 색상은 {my_car1.color}이며, 현재속도는 {my_car1.speed}km/h 입니다.')
# print(f'자동차2의 색상은 {my_car2.color}이며, 현재속도는 {my_car2.speed}km/h 입니다.')
# print(f'자동차3의 색상은 {my_car3.color}이며, 현재속도는 {my_car3.speed}km/h 입니다.')

#생성자 실습-매개 변수가 self만 있는 생성자
# #클래스 정의 부분
# class Car:
#     #속성 부여
#     color = '' #색상
#     speed = 0  #속도
#
#     #생성자 형성
#     def __init__(self):
#         self.color = '빨강'
#         self.speed = 10
#
#     #메서드 부여
#     def up_speed(self, value):
#         self.speed += value #속도 증가
#
#     def down_speed(self, value):
#         self.speed -= value #속도 감소
#
# #객체 생성
# my_car1 = Car() #빨강색과 10의 속도 자동 부여
# my_car2 = Car() #빨강색과 10의 속도 자동 부여
# my_car3 = Car() #빨강색과 10의 속도 자동 부여
#
# #출력
# print(f'자동차1의 색상은 {my_car1.color}이며, 현재속도는 {my_car1.speed}km/h 입니다.')
# print(f'자동차2의 색상은 {my_car2.color}이며, 현재속도는 {my_car2.speed}km/h 입니다.')
# print(f'자동차3의 색상은 {my_car3.color}이며, 현재속도는 {my_car3.speed}km/h 입니다.')

#생성자 실습-매개 변수가 self 말고도 있는 생성자
# #클래스 정의 부분
# class Car:
#     #속성 부여
#     color = '' #색상
#     speed = 0  #속도
#
#     #생성자 형성
#     def __init__(self, value1, value2):
#         self.color = value1
#         self.speed = value2
#
#     #메서드 부여
#     def up_speed(self, value):
#         self.speed += value #속도 증가
#
#     def down_speed(self, value):
#         self.speed -= value #속도 감소
#
# #객체 생성
# my_car1 = Car("빨강", 30)
# my_car2 = Car("파랑", 40)
# my_car3 = Car("노랑", 50)
#
# #출력
# print(f'자동차1의 색상은 {my_car1.color}이며, 현재속도는 {my_car1.speed}km/h 입니다.')
# print(f'자동차2의 색상은 {my_car2.color}이며, 현재속도는 {my_car2.speed}km/h 입니다.')
# print(f'자동차3의 색상은 {my_car3.color}이며, 현재속도는 {my_car3.speed}km/h 입니다.')

#상속 실습
#클래스 정의 부분
class Car: #부모 클래스
    speed = 0 #속도 부여

    def up_speed(self, value):
        self.speed += value
    def down_speed(self, value):
        self.speed -= value

class Sedan(Car): #자식 클래스1
    seat_num = 0 #좌석 부여

    def get_seat_num(self):
        return self.seat_num

class Truck(Car):
    capacity = 0
    def get_seat_num(self):
        return self.capacity

#변수 선언
sedan1 = None
Truck1 = None

#메인 코드 부분
sedan1 = Sedan()
truck1 = Truck()

sedan1.up_speed(100)
truck1.up_speed(80)

sedan1.seat_num = 5
truck1.capacity = 50

#출력
print(f'승용차의 속도는 {sedan1.speed}km/h, 좌석수는 {sedan1.get_seat_num()}개입니다.')
print(f'트럭의 속도는 {sedan1.speed}km/h, 총중량는 {truck1.capacity}톤입니다.')