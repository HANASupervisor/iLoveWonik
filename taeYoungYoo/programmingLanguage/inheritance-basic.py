# class Animal:
#     def eat(self):
#         print('먹는 중')


# class Dog(Animal):
#     def bark(self):
#         print('멍멍')


# my_dog = Dog()
# my_dog.bark()

# # 부모 클래스 메서드 사용 가능
# my_dog.eat()



# class Person:
#     def __init__(self,  name):
#         self.name = name

#     def greeting(self):
#         return f'안녕, {self.name}'
    

# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'
    

# class Dad(Person):
#     gene = 'XY'
    
#     def walk(self):
#         return '아빠가 걷기'
    

# class FirstChild(Dad, Mom):
#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
    

# baby1 = FirstChild('아가')
# print(baby1.cry()) # 첫째가 응애
# print(baby1.swim()) # 첫째가 수영
# print(baby1.walk()) # 아빠가 걷기
# print(baby1.gene) # XY

# class Car:
# 	def __init__(self):
# 		pass
	
# Car1 = Car()
# Car2 = Car()

# print(type(Car1))
# print(type(Car2))


# class Car :
#     color = ""
#     speed = 0

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 30

# print("자동차1의 색상은 %s이며, 현재속도는 %d km 입니다." % (myCar1.color, myCar1.speed))


# class Car :
#     speed = 0

#     def __init__(self, speed):
#         self.speed = speed

# Car1 = Car()

try:
    print(10/0)
except NameError:
    print('Variable is not defined')
except:
    print('Something went wrong')

# print(10/0)


# 계산기 문제
while True:
    try:
        user_input1 = int(input())
        user_input2 = int(input())

        result = user_input1 / user_input2
        print('계산 결과:', result)

        break
    except ValueError:
        print('숫자만 입려가셍 다시 입력합니다. \n')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다. 다시 입력합니다.\n')
