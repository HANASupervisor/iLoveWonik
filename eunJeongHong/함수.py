def hello(name,num):
    print(name, '님! 안녕하세요')
    print('합격을 진심으로 축하드립니다.')
    print('장소는 {}번 입니다'.format(num))

hello('재현',7)

def calc(a,b):
    r1=a+b
    return r1

result = calc(10,5)
print(result)
