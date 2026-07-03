def func1():
    print(1)


def func2():
    print(2)

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "0으로 나눌 수 없습니다."
    return num1 / num2