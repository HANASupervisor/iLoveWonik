'''
문자열에서 단어 분리: split()

str.split() 함수
 문자열에서 단어 분리 함수
 기본적으로 공백을 기준으로 단어를 분리함
 분리된 문자열은 리스트 형태로 리턴

split() 괄호안 기본값은 공백 중간에 ','어떤 것으로 구분할지 알려주면 그것으로 구분해줌
'''

s1 = 'Never put off till tomorrow what you can do today.'

split_str = s1.split() #공백을 기준으로 분리, 분리된 문자열은 리스트 형태로 리턴
print(split_str)
print(f'단어개수 : {len(split_str)}')

s2 = 'num, id, name, score'
print(s2.split(','))
