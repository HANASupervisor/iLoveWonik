'''
문자 개수 세기
str.count('문자') '문자가 나온횟수'
str.count('문자',start, end) '탐색 범위에서 문자가 나온횟수'
탐색 범위 : start ~ (end-1)

'''
s1 = 'This is a python string.'
print(s1.count('i'))

start = 0
end = 6

# start ~ end-1 사이에 'i' 문자가 나온 횟수
print(s1.count('i',start, end))
