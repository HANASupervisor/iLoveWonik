
numb=input('다섯자리 정수를 입력하시오!')#int사용x 
list_numb=[]

tot=0
for i in numb:
    tot+=int(i) #숫자를 int()문자로 변경
    list_numb.append(i)
    if list_numb.index(i) == 4:#마지막자리 숫자 위치가 4일때는 =을 출력
        print(i,end='=')
    else:
        print(i,end='+')
print(tot)

numb=int(input('다섯자리 정수를 입력하시오!'))

n1=numb // 10000
n2=(numb % 10000)// 1000
n3=(numb%1000)//100
n4=(numb%100)//10
n5=(numb%numb)
tot=n1+n2+n3+n4+n5
print(n1,'+',n2,'+',n3,'+',n4,'+',n5,'=',tot)


