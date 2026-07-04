'''
[start : end : step]
슬라이싱 : 범위 start ~ (end-1)까지 문자열 추출
end 포함되지 않음
step 생략되면 1로 간주
'''

word1 ='Python Programming'
word1_len = len(word1)
print(word1[:]) # 전체 문자열
print(word1[ : : ]) #전체 문자열
print(word1[1:]) # end가 생략되면, 문자열의 마지막 index
print(word1[:5]) # start가 생략되면 0부터 시작
print(word1[2:5])

# step 사용
print(word1[0:word1_len:2]) # 0 2 4 6 8 10 12
print(word1[1::2])# 1 3 5 7 9 11 13 15 17

'''
문자열은 불변 객체
 정수형, 실수형, 복소수형, 문자열, 튜플, 바이트, range형
 a의 값이 1에서 2로 바뀐것이 아니라, 객체의 메모리 주소가 변경됨

문자열은 변경 불가능
문자열 내부의 값 변경시 typeError 발생
'''
