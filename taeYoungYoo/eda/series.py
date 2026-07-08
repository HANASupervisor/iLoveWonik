# 딕셔너리 -> 시리즈 변환
import pandas as pd

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장
# 이때 딕셔너리를 변환하면 key는 인덱스 value는 값이 된다.
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(type(sr))

# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)



# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data =['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)



# 시리즈 인덱스
# 인덱스 배열은 변수 idx에 저장
idx = sr.index
print(idx) # RangeIndex(start=0, stop=5, step=1)



# 시리즈 인덱스
# 데이터 값 배열은 변수 val에 저장
val = sr.values
print(val) # ['2019-01-02' 3.14 'ABC' 100 True]



# 시리즈 배열을 구성하는 원소의 자료형
print(sr.dtype) # object



# 시리즈 인덱스
# 시리즈 배열의 크기
print(len(sr)) # 5



# 시리즈 배열 형태
print(sr.shape)



# 시리즈 배열의 차원
print(sr.ndim)



# 시리즈 원소 선택
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
sr = pd.Series(tup_data)
print(sr)



# # 시리즈 원소 선택
print(sr[0])
# # print(sr['이름'])



# 여러개의 원소를 선택(인덱스 리스트 활용)
print(sr[1: 2])
print('\n')
# print(sr['생년월일': '성별'])


pd.Series()

value = pd.Series(5, index=['a', 'b', 'c'])
print(value)


# 딕셔너리 데이터 프레임 반환
dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터 프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df))

print(df)

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 길이 출력
print(len(sr))