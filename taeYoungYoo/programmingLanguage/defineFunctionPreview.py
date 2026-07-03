# 파이썬 함수 요약
# 1. 함수란? 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음이다. 

num1 = 5
num2 = 3
sumResult = num1 + num2
print(sumResult)

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    '''
    이것은 두 수를 받아 두수의 합을 반환하는 함수입니다. -> docstring
    '''
    return num1 + num2 # -> return value


sum_result = get_sum(num1, num2)
print(sum_result)


# 함수 호출
print(get_sum(100, 50))










