'''
구분자문자열. join()
구분자 문자열. join(문자열 or 문자열 리스트) 함수
 구분자 문자열과 문자열 리스트의 요소들을 연결해 새로운 문자열을 만듬
'''

#콤마 및 공백을 구분자로 사용해 리스트의 각 요소를 결합
str1 = ', '.join(['apple', 'banana', 'grape'])
print(str1)

# 문자열 사이에 -기호 추가 
str2 = '-'.join("010 1234 5678".split()) # 010 1234 5678 문자열을 공백을 기준으로 구분을 한 후 -로 결합하겠다 ㅅㅂ
print(str2)

# 빈 문자열을 구분자로 사용 문자 결합
chars = ["a", "b", "c"]
str3 = ''.join(chars)
print(str3)

# 공백을 구분자로 사용하여 단어 결합
words = ['python','is','easy']
str4 = ' '.join(words)
print(str4)

