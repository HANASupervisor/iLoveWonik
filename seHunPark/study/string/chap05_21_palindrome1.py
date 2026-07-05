'''
회문 앞으로 읽으나 뒤로 읽으나 동일한 문장

'''

'''
방법 1: 각문자를 하나씩 비교
'''

word = input('문자열을 입력하세요: ')
left = 0
right = len(word)-1
while True:
    char1 = word[left]
    char2 = word[right]

    if char1 != char2:
        print('회문이 아닙니다. ')
        break

    left += 1
    right -= 1


    if left > right:
        print('회문입니다.')
        break

'''
방법 2: 슬라이싱 활용
'''

str1 = input('문자열을 입력하세요: ')

str2 = str1[::-1] # 문자열을 거꾸로 만듦

print(f'원본: {str1}')
print(f'역순: {str2}')

if str1 == str2:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')