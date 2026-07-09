"""
플립러닝 코드 작성
260707
김찬영
"""
import pandas as pd

##Ex 1-1
# # k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
# dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
#
# # 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장
# sr = pd.Series(dict_data)
#
# # 변수 sr의 자료형 출력
# print(type(sr))
#
# #변수 sr에 저장되어 있는 시리즈 객체를 출력
# print(sr)

##Ex 1-2
# # 리스트를 시리즈로 변환하여 변수 sr에 저장
# list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
# sr = pd.Series(list_data)
# print(sr)
#
# # 인덱스 배열은 변수 idx에 저장
# idx = sr.index
# print(idx)
#
# # 데이터 값 배열은 변수 val에 저장
# val = sr.values
# print(val)
#
# # 시리즈 배열을 구성하는 원소의 자료형
# print(sr.dtype)
#
# # 시리즈 배열의 크기
# print(len(sr))
#
# # 시리즈 배열의 형태
# print(sr.shape)
#
# # 시리즈 배열의 차원
# print(sr.ndim)

##Ex 1-3
# 튜플을 시리즈로 변환(인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 원소를 1개 선택
print(sr.iloc[0]) #sr의 1번째 원소를 선택(정수형 위치 인덱스)
print(sr['이름']) #'이름' 라벨을 가진 원소를 선택(인덱스 이름)

# 여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr.iloc[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])

# 여러 개의 원소를 선택
print(sr[1 : 2])
print('\n')
print(sr['생년월일' : '성별'])

# 빈 시리즈 실습
print(pd.Series())
print(pd.Series(5))
print(pd.Series(5, index=["a", "b", "c"]))
