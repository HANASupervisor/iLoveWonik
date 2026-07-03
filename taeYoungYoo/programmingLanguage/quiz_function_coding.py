'''
1. “파이썬”을 출력하는 print_python() 함수를 선언하고, print_python() 함수를 호출하여 실행해
보자.
'''

def print_python():
    print('파이썬')

print_python()

'''
2. “환영합니다.”를 출력하는 welcome() 함수를 선언해보자. for 문을 이용하여 3회 반복하면서
welcome() 함수를 호출하여 실행해보자.
'''
def welcome():
    print('환영합니다.')

for iteration in range(3):
    welcome()


'''
3. 이름(예:홍길동)을 매개 변수로 전달 받으면 “환영합니다. 홍길동 님”으로 출력하는 welcome()
함수를 선언해보자. 이름을 입력 받아 welcome() 함수를 호출하여 실행해보자.
'''
def welcome(name):
    print(f'환영합니다. {name} 님')

welcome(input('이름을 입력해주세요'))


'''
4. 문자열과 횟수를 매개 변수로 전달 받으면 횟수만큼 문자열을 반복하여 출력하는 print_str() 함
수를 선언해보자. 문자열과 횟수를 각각 입력 받아 print_str() 함수를 호출하여 실행해보자.
'''
def print_str(char, time):
    for _ in range(time):
        print(char)

char = input('문자열: ')
time = int(input('횟수: '))
print_str(char, time)


'''
5. 이름(예:홍길동)과 환영메시지(예:환영합니다.)를 매개 변수로 전달 받으면 “환영합니다. 홍길
동 님”으로 출력하는 welcome() 함수를 선언해보자. 단, 환영메시지의 디폴트 매개변수 값은 “환

영합니다.”로 선언한다. 만약 welcome() 함수를 호출할 때 welcome(n, “반갑습니다.”)와 같이 환
영메시지 인수를 지정할 경우 “환영합니다.” 대신에 “반갑습니다.”를 출력한다.
'''
def welcome(name, message='환영합니다.'):
    print(f'{message} {name} 님')

welcome(input('이름을 입력해주세요'))
welcome(input('이름을 입력해주세요'), input('메시지를 입력해주세요'))


'''
6. 원의 반지름을 입력 받아 원의 넓이를 구하여 반환하는 circle_area() 함수를 선언해보자. 반지
름을 입력 받아 함수를 호출하고 결과를 반환 받아 출력해보자.
'''
import math
radius = float(input('반지름: '))

def circle_area(radius):
    area = math.pi *(radius ** 2)
    return area

print(f'반지름 {round(radius)}의 넓이: {round(circle_area(radius),4)}')


'''
7. 정수를 전달 받아 양수이면 1, 0이면 0, 음수이면 -1을 반환하는 pzn() 함수를 선언해보자. 그리
고 while 문을 이용하여 무한 반복하면서 사용자로 부터 정수를 입력 받아 pzn() 함수를 호출하고,
함수의 결과를 전달 받아 결과가 1이면 “양수”를 출력하고, -1이면 “음수”를 출력하고, 0이면 “0”을
출력하고 무한 반복을 종료해보자.
'''


def pzn(decimal_num):
    if decimal_num > 0:
        return 1
    elif decimal_num == 0:
        return 0
    else:
        return -1
    
while True:
    decimal_num = int(input('정수: '))
    result = pzn(decimal_num)

    if result == 1:
        print('양수')
    elif result == 0:
        print('0')
    else:
        print('음수')
    break


'''
8. 함수의 매개변수로 2개 이상의 정수를 가변적으로 전달받아 합계를 구하여 반환하는 vsum()
함수를 선언해보자. vsum() 함수를 vsum(2, 3), vsum(2, 3, 4), vsum(2, 3, 4, 5) 순으로 인수의 수
를 변경하면서 호출해보자.
'''
def vsum(*args):
    summation = 0
    con_list =[]
    for num in args:
        summation += num
        con_list.append(num)
    
    for idx in range(len(con_list)):
        if idx >= len(con_list) -1:
            print(f'{con_list[idx]} = {summation}')
        else:
            print(f'{con_list[idx]} + ', end='')

vsum(2,3)
vsum(2,3,4)
vsum(2,3,4,5)