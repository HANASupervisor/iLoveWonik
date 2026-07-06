# class Car:
#     color = ''
#     def __init__(self, speed):
#         self.speed = speed
    
#     def upSpeed(self, value):
#         self.speed += value

#     def downSpeed(self, value):
#         self.speed -= value

# car = Car(3)
# car.upSpeed(3)
# print(car.speed)





class Car:
    # 클래스 변수
    color = ''
    speed = 0

    # init을써서 생성자를 만드는거 인스턴스 변수
    # def __init__(self, color, speed):
    #     self.color = color
    #     self.speed = speed

    @classmethod
    def upSpeed(self, value):
        self.speed += value

    @classmethod
    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

print("자동차의 색상 %s 현재 속도 %d km" % (myCar1.color, myCar1.speed))
print("자동차의 색상 %s 현재 속도 %d km" % (myCar2.color, myCar2.speed))
print("자동차의 색상 %s 현재 속도 %d km" % (myCar3.color, myCar3.speed))

myCar1.upSpeed(10)
myCar2.upSpeed(20)
myCar3.upSpeed(30)

print("자동차의 색상 %s 현재 속도 %d km" % (myCar1.color, myCar1.speed))
print("자동차의 색상 %s 현재 속도 %d km" % (myCar2.color, myCar2.speed))
print("자동차의 색상 %s 현재 속도 %d km" % (myCar3.color, myCar3.speed))
# 알게 된점 한가지 class 변수인 상태에서 갑을 할당을 때리는 순간 내부적으로 인스턴스 변수로 변환된다.  

class Car:
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        print('현재 속도(슈퍼 클래스):%d' % self.speed)


class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print('현재 속도(서브 클래스): %d' % self.speed)


class Truck(Car):
    pass


# 변수 선언
sedan1, truck1 = None, None

# 메인 코드 부분
truck1 = Truck()
sedan1 = Sedan()

print('트럭 ->', end=' ')
truck1.upSpeed(200)

print('승용차 ->', end=' ')
sedan1.upSpeed(200)











print('hello'.upper())
print(str.upper('hello'))


class Car:
    def __init__(self):
        self.color = '빨강'
        self.speed = 0

    @classmethod
    def upSpeed(cls, value):
        cls.speed += value

    @classmethod
    def downSpeed(cls, value):
        cls.speed -= value


class Car:
    color = '빨강'
    speed = 0

    @classmethod
    def upSpeed(cls, value):
        cls.speed += value

    @classmethod
    def downSpeed(cls, value):
        cls.speed -= value