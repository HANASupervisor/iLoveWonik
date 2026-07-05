'''
str.find('문자열')
    검색된 문자열의 시작 인덱스 리턴 : 왼쪽에서 탐색 
     but 검색된 문자나 문자열이 없으면 -1리턴

str.rfind('문자열') : reverse find
    검색된 문자열의 시작 인덱스 리턴 : 문장의 처음부터 계산된 인덱스 리턴
    뒤(오른쪽 끝)에서 부터 검색:
'''

s1 = "this is a python string" 
print(s1.find('n'))

index = s1.find('s')
if index == -1:
    print("검색 결과가 없습니다.")
else:
    print(f'검색 위치: {index}')

print(s1.rfind('s')) # 문장의 처음부터 계산된 인덱스 리턴

#find는내가 원하는 위치에 있는 n을 찾을 수가 없음 하지만 index는 내가 원하는 위치에서 어느 구간에 있는지 확인가능