# # 더하기
# def plus(num1, num2):
#     result = num1 + num2
#     return result

# num1 = 200
# num2 = 300
# print(f"{num1}과 {num2}의 합은 {plus(num1, num2)} 입니다.")

# # 입력 자유롭게 받아서 쓰기
# def multiplus(*args):
#     summation = 0
#     value_list = [*args]
#     print(value_list)

#     for num in value_list:
#         summation += num
#     return summation


# print(multiplus(1,2,3,4,5,6,7,88,5,5,4,45,6,45,6,4,4))



# # 함수 정의부분
# def calc(v1, v2, op)
#     result = 0
#     if op == "+":
#         result = v1 + v2
#     elif op == "-":
#         result = v1 - v2
#     elif op == "*":
#         result = v1 * v2
#     elif op == "/":
#         result = v1 / v2
#     else:
#         print("연산자를 잘못 입력하셨습니다.")
#     return result


# # 변수 선언 부분
# res = 0
# var1, var2, oper = 0, 0, ""

# # 메인코드 부분
# oper = input("연산자 입력(+,-,*,/): ")
# var1 = int(input("첫 번째 숫자 입력: "))    
# var2 = int(input("두 번째 숫자 입력: "))

# # 함수 실행부분
# res = calc(var1, var2, oper)
# print(f"{var1} {oper} {var2} = {res}")


# while True:
#     oper = input("연산자 입력(+,-,*,/): ")
#     var1 = int(input("첫 번째 숫자 입력: "))    
#     var2 = int(input("두 번째 숫자 입력: "))

#     # 함수 실행부분
#     res = calc(var1, var2, oper)
#     print(f"{var1} {oper} {var2} = {res}")


# LEGB Rule
# Built-in scope

# len, print 같은 파이썬 내장 함수가 있는 영역
x = 'global x'

def outer():
    x = 'enclosing x'
    def inner():
        x = 'local x'
        print('inner 안에서 x: ', x)
    
    inner()

outer()


# 이거 3문제 맞추면 커피 사드림



a = 1
b = 2

def enclosed():
    a = 3
    c = 3

    def local(c):
        print(a, b, c) # ?

    local(500)
    print(a, b, c) # ?

    enclosed()
    print(a, b) # ?


a = print(2)
print(a)


# # None 
# def alpha(dd):
#     print(1)

# tt = alpha(2)
# print(tt)

# def func1() :
#     result = 100
#     return result

# def func2():
#     print("반환값 없는 함수 실행")

# ## 변수 선언 부분
# hap = 0

# ## 메인 코드 부분
# hap = func2()
# # 이 hap에서 에러가 뜨는건 포맷은 %d인데 정수가 들어온게아니라 None이 들어와서 에러가 뜬거임
# # 
# print("func2()에서 돌려준 값 ==> %d" % hap)


def func3(a: int, b: int = 2, c: int = 2) -> int:
    result = a + b + c
    return result 

# print(func3(1,3)) # error
print(func3(1, c = 3))
# print(func3(1,b = 3, 4))


def para_func(*args, **kwargs):
    print(type(args))
    print(args)
    summation = 0
    for num in args: # args는 튜플임. 리스트 아님
        summation += num
    
    return summation

para_func(1,2,3,4,5,6,7,8,9, 10)

a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(type(a))


# 
# def dict_func(**kwargs):
#     # print(type(args))
#     # print(args)
#     print(type(kwargs))
#     print(kwargs)
#     return kwargs

# dict_func(1,2,3,4,5,6,7,8,9,10, name = "홍길동", age = 20)




# 이거 됨?
def aa(a, b, c):
    return a + b + c

print(aa(1, 2, 3))


# 이거 됨?
def aa(a, b=2, c=3):
    return a + b + c

print(aa(1, 3))




