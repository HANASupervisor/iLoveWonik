# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email


class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email)
        # Person.__init__(name, age, number, email) # 위에 super하는 코드나 이코드나 똑같음 하지만 부모케이스 개발중 이름이 바뀔경우 유지보수 위해서 super가 나음
        self.student_id = student_id


# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f"Value from ParentA: {self.value_a}")


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()
        print(f'Value from child: {self.value_c}')


child = Child()
child.show_value()

print(child.value_c) # Child
print(child.value_a) # ParentA

# print(child.value_b) # 부모가 아니라 조상노드 참조하는건 반영하지않음


# 클래스 상속 개념에서 반드시 super메서드를 이용해야하는 이유
class Parent:
    def __init__(self):
        self.name = "부모"

class Child(Parent):
    def __init__(self):
        self.age = 20

child = Child()
# print(child.name) # error: 'Child' object has no attribute 'name' 
#                   # Parent의 __init__()이 실행되지 않아서 self.name이 생성되지 않았기 때문에 에러 발생
print(child.age) # 


# 그렇다면 mro의 흐름은 어떻게 되는가 공부해보겠다
# mro가 필요한 이유 
# 부모 클래스들이 여러번 액세스 되지 않도록
# 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고,
# 각 부모를 오직 한번만 호출하고,
# 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조형성

class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')


print(D.mro())
print(D.__mro__)

