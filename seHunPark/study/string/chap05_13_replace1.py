'''
문자열 변경함수 replace(검색단어, 변경단어[,변경횟수]) 맨마지막 생략가능 살짝 한글 변경기능 느낌
    - 변경된 문자열을 반환하며, 원본 문자열은 변경 안됨
        - 변경 횟수가 없으면, 모두 변경
        - 검색단어가 원본 문자열에 없으면, 원본 문자열 반환

        # 문자열, 튜플 불변  c컨셜(순서) 보고 가변인지 불변인지 보고
'''

a = 'a,b,c,d,e'
print(a.replace(',','/')) # 모두 변경 
# 위에서 변경 됐는데 밑에꺼에서 문자열이 변경됨, 
# 되는이유 : 문자열이라서 원래 문자열자체는 수정불가능 replace함수로 변경은 했지만 원본 변경안됨
print(a.replace(',','/',2))
print(a.replace(',','/',1)) # a/b,c,d,e 1회 변경
# print(a.replace(''))

text = "I like bananas"
replace_str = text.replace('orange', 'apple')
print(f'repalce_str: {replace_str}')

# 변경된 문자열을 저장하는법
    # 변수지정해서 대입
x = text.repalce("bananas", "apples") 
print(f'text: {text}')
print(f'x: {x}')

y = text.replace(' ', ' ')
print(f'y: {y}')

