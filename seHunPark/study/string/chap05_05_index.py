'''
문자열 인덱싱
문자열 대괄호[index]를 사용해 문자를 추출하거나 개별문자에 접근하는 것
인덱싱
    - 문자열에 포함된 각 문자에 매겨진 번호
    - 음수 인덱스도 존재
    ex) 양수  0   1   2   3   4   5
        숫자  p   y   t   h   o   n
        음수 -6  -5  -4  -3 -2  -1
'''

# 문자열의 길이 : len("문자열")

word = 'Python'
print(f'len:{len(word)}')

print(f'index[0] : {word[0]}')
print(f'index[5] : {word[5]}')
print(f'index[-1] : {word[-1]}')