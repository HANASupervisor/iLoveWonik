"""
플립러닝 코드 작성
260707
김찬영
"""
import pandas as pd

##Ex 1-4
# # 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
# dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
#
# # 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
# df = pd.DataFrame(dict_data)
#
# # df의 자료형 출력
# print(type(df))
#
# # 변수 df에 저장되어 있는 데이터프레임 객체를 출력
# print(df)

##Ex 1-5
# # 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
#                   index=['준서', '예은'],
#                   columns=['나이', '성별', '학교'])
#
# # 데이터프레임 출력하기
# print(df)
#
# # 행 인덱스 확인하기
# print(df.index)
#
# # 열 이름 확인하기
# print(df.columns)
#
# # 행 인덱스, 열 이름 변경하기
# df.index = ['학생1', '학생2']
# df.columns = ['연령', '남녀', '소속']
#
# print(df)
# print('\n')
# print(df.index)
# print('\n')
# print(df.columns)

##Ex 1-6
# # 행 인덱스/열 이름 지정하여 데이터프레임 만들기
# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
#                   index=['준서', '예은'],
#                   columns=['나이', '성별', '학교'])
#
# # 행 인덱스, 열 이름 확인하기
# print(df)
#
# # 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
# df = df.rename(columns={'나이':'연령', '성별':'남녀','학교':'소속'})
#
# #df 출력(변경 후)
# print(df)
#
# # df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
# df = df.rename(index={'준서':'학생1', '예은':'학생2'})
#
# #df 출력
# print(df)

##Ex 1-7
# # DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
# exam_data = {'수학' : [90,80,70], '영어' : [98, 89, 95],
#              '음악' : [85,95,100], '체육' : [100, 90, 90]}
#
# df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
# print(df)
#
# # 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제
# df2 = df.copy()
# df2 = df2.drop('우현')
# print(df2)
#
# # 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row) 삭제
# df3 = df.copy()
# df3 = df3.drop(['우현', '인아'], axis=0)
# print(df3)
#
# # 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 2개 행(row) 삭제
# df4 = df.copy()
# df4 = df.drop(['우현', '인아'], axis='index')
# print(df4)
#
# # 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 1개 행(row) 삭제
# df5 = df.copy()
# df5 = df.drop(index = ['우현'])
# print(df5)

##Ex 1-8
# # DataFrame() 함수로 데이터프레임 변환. 변환 df에 저장
# exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
#
# df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
# print(df)
#
# # 데이터프레임 df를 복제하여 변수 df2에 저장. df2의 1개 열(column) 삭제
# df2 = df.copy()
# df2 = df.drop('수학', axis=1)
# print(df2)
#
# # 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 열(column) 삭제
# df3 = df.copy()
# df3 = df3.drop(['영어', '음악'], axis=1)
# print(df3)
#
# # 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 2개 열(column) 삭제
# df4 = df.copy()
# df4= df4.drop(['영어', '음악'], axis='columns')
# print(df4)
#
# # 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 1개 열(column) 삭제
# df5 = df.copy()
# df5 = df5.drop(columns=['수학'])
# print(df5)

##Ex 1-9
# # DataFrame() 함수로 데이터프레임 변환. 변환 df에 저장
# exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}
#
# df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
#
# # 데이터프레임 출력
# print(df)
#
# # 행 인덱스를 사용하여 행 1개 선택
# label1 = df.loc['서준']
# position1 = df.iloc[0]
# print(label1)
# print('\n')
# print(position1)
#
# # 행 인덱스를 사용하여 2개 이상의 행 선택
# label2 = df.loc[['서준', '우현']]
# position2 = df.iloc[[0, 1]]
# print(label2)
# print('\n')
# print(position2)
#
# # 행 인덱스의 범위를 지정하여 행 선택
# label3 = df.loc['서준' : '우현']
# position3 = df.iloc[0 : 1]
# print(label3)
# print('\n')
# print(position3)

##Ex 1-10
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [ 100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
# print('\n')
# print(type(df))
#
# # '수학' 점수 데이터만 선택. 변수 math1에 저장
# math1 = df['수학']
# print(math1)
# print('\n')
# print(type(math1))
#
# # '영어' 점수 데이터만 선택. 변수 english에 저장
# english = df.영어
# print(english)
# print('\n')
# print(type(english))
#
# # '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
# music_gym = df[['음악', '체육']]
# print(music_gym)
# print('\n')
# print(type(music_gym))
#
# # '수학' 점수 데이터만 선택, 변수 math2에 저장ㄹ
# math2 = df[['수학']]
# print(math2)
# print('\n')
# print(type(math2))
#
# # 슬라이싱
# print(df.iloc[: : 2])
# print(df.iloc[0:3:2])
# print(df.iloc[::-1])

##Ex 1-11
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
#
# # '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 반영
# df = df.set_index('이름')
# print(df)
#
# # 데이터프레임 df의 특정 원소 1개 선택('서준'의 '음악' 점수)
# a = df.loc['서준', '음악']
# print(a)
# b = df.iloc[0, 2]
# print(b)
#
# # 데이터프레임 df의 특정 원소 2개 이상 선택('서준'의 '음악', '체육' 점수)
# c = df.loc['서준', ['음악', '체육']]
# print(c)
# d = df.iloc[0, [2,3]]
# print(d)
# e =df.loc['서준', '음악' : '체육']
# print(e)
# f = df.iloc[0,2:]
# print(f)
#
# # df 2개 이상의 행과 열에 속하는 원소들 선택('서준', '우현'의 '음악', '체육'의 점수)
# g = df.loc[['서준', '우현'], ['음악', '체육']]
# print(g)
# h = df.iloc[[0,1], [2,3]]
# print(h)
# i = df.loc['서준' : '우현', '음악' : '체육']
# print(i)
# j = df.iloc[0:2, 2:]
# print(j)

##Ex 1-12
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
#
# # 데이터프레임 df에 '국어' 점수 열(column) 추가. 데이터 값은 80 지정
# df['국어'] = 80
# print(df)
#
# # 데이터프레임 df에 '미술' 점수 열(column) 추가. 데이터는 [80, 90, 100] 지정
# df['미술'] =[ 80, 90, 100]
# print(df)

##Ex 1-13
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
# print('\n')
#
# # 새로운 행(row) 추가 - 같은 원소 값 입력
# df.loc[3] = 0
# print(df)
#
# # 새로운 행(row) 추가 - 원소 값 여러 개의 배열 입력
# df.loc[4] = ['동규', 90, 80, 70, 60]
# print(df)
#
# #새로운 행(row) 추가 - 기존 행 복사
# df.loc['행5'] = df.loc[3]
# print(df)

##Ex 1-14
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
#
# # '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
# df = df.set_index('이름')
# print(df)
#
# # 데이터프레임 df의 특정 원소를 변경하는 방법: '서준'의 '체육' 점수
# df.iloc[0][3] = 80
# print(df)
#
# df.loc['서준']['체육'] = 90
# print(df)
#
# df.loc['서준', '체육'] = 100
# print(df)
#
# # 데이터프레임 df의 원소 여러 개를 변경하는 방법: '서준'의 '음악', '체육' 점수
# df.loc['서준', ['음악', '체육']] = 50
# print(df)
#
# df.loc['서준', ['음악', '체육']] = 100, 50
# print(df)

##Ex 1-15
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
#
# # 데이터프레임 df를 전치하기(메소드 활용)
# df = df.transpose()
# print(df)

# # 데이터프레임 df를 다시 전치하기(클래스 속성 활용)
# df = df.T
# print(df)

##Ex 1-16
# # DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
# exam_data = {'이름' : [ '서준', '우현', '인아'],
#              '수학' : [ 90, 80, 70],
#              '영어' : [ 98, 89, 95],
#              '음악' : [ 85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
#
# #특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정
# ndf = df.set_index(['이름'])
# print(ndf)
#
# ndf2 = ndf.set_index('음악')
# print(ndf2)
#
# ndf3 = ndf.set_index(['수학', '음악'])
# print(ndf3)

##Ex 1-17
# # 딕셔너리를 데이터프레임으로 변환
# dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
#
# # 인덱스를 [r0, r1, r2]로 지정
# df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
# print(df)
#
# # 인덱스를 [r0, r1, r2, r3, r4]로 재지정
# new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
# ndf = df.reindex(new_index)
# print(ndf)
#
# # reindex로 발생한 NaN 값을 숫자 0으로 채우기
# new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
# ndf2 = df.reindex(new_index, fill_value=0)
# print(ndf2)

##Ex 1-18
# # 딕셔너리를 데이터프레임으로 변환
# dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
#
# # 인덱스를 [r0, r1, r2]로 지정
# df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
# print(df)
#
# # 행 인덱스를 정수형으로 초기화
# ndf = df.reset_index()
# print(ndf)
#
# # 행 인덱스를 정수형으로 초기화하고, 기존 인덱스의 열 이름을 지정
# ndf2 = df.reset_index(names=['C00'])
# print(ndf2)
#
# # 행 인덱스를 초기화하고, 기존 인덱스를 삭제
# ndf3 = df.reset_index(drop=True)
# print(ndf3)

##Ex 1-19
# # 딕셔너리를 데이터프레임으로 변환
# dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
#
# # 인덱스를 [r0, r2, r1]로 지정
# df = pd.DataFrame(dict_data, index = ['r0', 'r2', 'r1'])
# print(df)
#
# # 내림차순으로 행 인덱스 정렬
# ndf = df.sort_index(ascending = False)
# print(ndf)
#
# # 오름차순으로 행 인덱스 정렬
# ndf2 = df.sort_index(ascending = True)
# print(ndf2)

##Ex 1-20
# 딕셔너리를 데이터프레임으로 변환
dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,10,11], 'c4' : [15,14,14]}

# 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)

# c1 열을 기준으로 내림차순 정렬
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)

# c2 열을 기준으로 오름차순 정렬
ndf2 = ndf.sort_values(by='c2', ascending=True)
print(ndf2)

# c3 열을 기준으로 내림차순 정렬, c4 열을 기준으로 오름차순 정렬
ndf3 = ndf.sort_values(by=['c3', 'c4'], ascending=[False, True])
print(ndf3)