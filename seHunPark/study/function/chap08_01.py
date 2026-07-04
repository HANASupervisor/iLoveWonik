'''
함수
특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것
함수는 작업에 필요한 데이터를 전달 받기 가능 : 입력
작업이 완료된 후에는 작업의 결과를 호출자에게 반환가능
'''

# 함수정의
def get_area(radius):  #함수헤더 함수이름 매개변수 
    area = 3.14 * radius**2
    return area

# 함수 호출
    # 함수의 실행이 끝나면 호출한 위치로 돌아감
    # 호출 해야 함수가 실행됨

x = get_area(3)
print(x)

#  매개변수
    # 정의할때
# 인수
    # 호출
# 반환값
    #함수가 호출된 곳으로 반환하는 결과값
def get_sum(start, end): #start end는 매개변수
    sum = 0
    for i in range(start, end+1): # 
        sum += i
    return sum

result1 = get_sum(1,10) #1과10은 인수
result2 = get_sum(1,20)
print(result1, result2)


