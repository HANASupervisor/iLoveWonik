'''
문자열
큰 따옴표, 작은 따옴표 사용
여러줄의 문자열 3개의 큰 따옴표 도는 3개의 작은 따옴표 사용
'''

# 작은 따옴표 사용
s1 = str('Hello')
s2 = 'Hello'

# 큰 따옴표 사용
s1 = "Hello"
s2 = "world"
s3 = s1 + s2

print(s3)

multi_line_str = print("첫 번째 줄입니다." \
                        "두 번째 줄입니다." \
                        "세 번째 줄입니다." \
                        "네 번째 줄입니다.")

multi_line_string = \
'''
첫 번쨰 줄입니다.
두 번째 줄입니다.
세 번째 줄입니다.
'''

print(multi_line_string)

'''
문자열을 표시할때 '',  "" , ''' ''', str 코드가 긴경우 \
'''