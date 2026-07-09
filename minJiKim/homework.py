#1
def print_python() :
    print('파이썬')
print_python()


#2
def welcome() :
    print('환영합니다.')
for i in range(3) :
    welcome()


#3
def welcome(name) :
    print(f'환영합니다. {name} 님')
    
n = input('이름: ')
welcome(n)


#4
def print_str(st, cnt) :
    for i in range(0, cnt) :
        print('파이썬')
        
s= input('문자열: ')
c=int(input('횟수: '))

print_str(s,c)



#5
def welcome(name, msg='환영합니다.') :
    print(f'{msg} {name}님')

n = input('이름 : ')
welcome(n)
welcome(n, '반갑습니다.')


#6
def circle_area(radius) :
    area = radius**2 * 3.141592
    return area
    
r = int(input('반지름 : '))
print(f'반지름 {r}의 넓이: {circle_area(r)}')


#7                                       #def pzn(num:int) -> int:
def pzn (num):      #num에 int를 입력해야하고, int로 출력이 됨
    """이거 flag 함수면"""
    if num > 0 :
        return 1
    elif num < 0 :
        return -1
    else :
        return 0

#if __name__ = "__main__":      #밑에 함수를 메인함수로 인식
while True :
    n = int(input('정수: '))
    flag = pzn(n)

    if flag == 1 :
        print('양수')
    elif flag == -1 :
        print('음수')
    else :
        print(0)
        break
                     

#8
def vsum(*num) :
    sum = 0
    for i in num :
        if i == num[len(num)-1] :
            print(i, end='=')
            sum = sum + i
        else :
            print(i, end='+')
            sum = sum + i
    return sum

total = 0

total = vsum(2,3)
print(total)
total = vsum(2,3,4)
print(total)
total = vsum(2,3,4,5)
print(total)

#정답
def vsum(*num) :
    sum = 0
    for i in range (len(num)) :
        print(num[i], end='')
        if i  < len(num)-1 :
            print('+', end='')
        sum = sum + int(num[i])
    print('=', sum)
vsum(2,3,4,5)









    


