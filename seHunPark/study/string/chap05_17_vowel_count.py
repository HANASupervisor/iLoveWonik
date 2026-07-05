'''
str.isalnum() 문자열이 알파벳과 숫자로만 있으면 True
str.isalpha() 문자열이 알파벳으로 이루어져있으면 True
isdigit() 문자열이 숫자로만 이루어져있으면 True

'''
'''
자음과 모음의 개수를 계산하는 프로그램을 작성해보자
'''


text = input('문자열을 입력하시오: ')
word = text.lower()
vowles = 0 #모음
consonants = 0 #자음

if len(text) > 0 and text.isalpha(): # text가 있는지, 그리고 알파벳으로 이루어져있는지
    for char in word:
        if char in 'aeiou':
            vowles = vowles + 1
        else:
            consonants = consonants + 1

print(f'모음의 개수 : {vowles}, 자음의 개수 : {consonants}')



