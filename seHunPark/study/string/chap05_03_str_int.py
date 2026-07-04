'''
문자열 + 정수 연산 : TypeError 발생
서로 다른 타입은 '+'연산 적용 안됨 
'''

# print('student' + 10)

# 정수를 문자열로 변환 : str(숫자)
print('student' + str(10))

# 문자열을 정수로 변환 : int("숫자")

width = int("150")
height = int("180")

print(width + height)
