from mymodule import *
# 메인 코드 부분
in1 = float(input('첫 번째 숫자 입력: '))
in2 = float(input('두 번째 숫자 입력: '))
operator = input('연산자 입력(+,-,*,/): ')

print()
print('*** 모듈로 작성한 계산기 호출 결과 ***')
if operator == '+':
    print(f'{in1} + {in2} = {plus(in1, in2)}')
elif operator == '-':
    print(f'{in1} - {in2} = {minus(in1, in2)}')
elif operator == '*':
    print(f'{in1} * {in2} = {multiply(in1, in2)}')
elif operator == '/':
    print(f'{in1} / {in2} = {divide(in1, in2)}')
else:
    print('연산자를 잘못 입력하셨습니다.')

print(1, sep=None, end=None)
print(2, sep=None, end=None)


