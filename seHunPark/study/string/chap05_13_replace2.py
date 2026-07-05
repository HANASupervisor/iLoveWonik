'''
문자열 내부 공백 제거 또는 천 단위 콤마제거
'''

# 문자열 내부의 공백 제거
text = 'Hello, World! '
new_text = text.replace(' ','')
print(new_text)

# 천단위 콤마 제거
num_str1 = '2,500,600'
num_str2 = '123,000'

num_str1 = num_str1.replace(',','') # 문자열 내부의 콤마 제거(빈문자열 사용)
num1 = int(num_str1) #문자열을 숫자로 변경

num_str2 = num_str2.replace(',', '') # 문자열 내부의 콤마 제거
num2 = int(num_str2) #문자열을 숫자로 변경

print(f'num1 + num2 = {num1 + num2}') # 안에 수식쓰기 가능
