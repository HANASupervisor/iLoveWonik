'''
str. index('검색문자열', start, end)
    검색된 문자열의 첫 번째 인덱스 리턴
    검색 문자나 문자열이 없으면 오류 발생(ValuseError)
'''
'''

    a b c d e f g a b c  d e  f   g 
    0 1 2 3 4 5 6 7 8 9 10 11 12 13
'''
      
msg = 'abcdefgabcdefg'

print(msg.index('c')) # c가 몇번째 위치에 있는지 말해줌
print(msg.index('fg'))
print(msg.index('c', 0, 5))

if 'z' in msg: # z가 문자열 내부에 있으면
    print(msg.index('z')) # 몇번째 위치에 있는지 표시해라
else:
    print(f'문자열(msg) 내부에 문자 z가 없습니다.')