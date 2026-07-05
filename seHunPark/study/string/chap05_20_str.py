'''
문자열을 조사해서
알파벳의 문자의 개수, 숫자의 개수, 스페이스의 개수를 
출력하는 프로그램을 작성해라 
'''

# str_put = input('문자열을 입력하시오: ')

# alphas = 0
# digits = 0
# spaces = 0

# statement = str_put.strip()

# for c in str_put:
#     if c.isalpha(): #문자열이 알파벳이면 True
#         alphas = alphas + 1
#     if c.isdigit(): # 문자열이 숫자로 되어있으면 True
#         digits = digits + 1
#     if c.isspace(): 
#         spaces = spaces + 1

# print("알파벳 문자의 개수=", alphas)
# print("숫자 문자의 개수=", digits)
# print("단어 개수=", spaces+1)


s1 = "This is a Python string."

print('s1.isalpha():', s1.isalpha()) # 공백이 있어서 False
print('s')