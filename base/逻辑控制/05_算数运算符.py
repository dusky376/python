a = 10
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')   #整除
print(f'{a} %  {b} = {a % b}')   #取余
print(f'{a} ** {b} = {a ** b}')  #幂运算
a ** b
print(f'{a} %  {b} = {a % b}')

print(f'{a}<{b},{a<b}')
print(f'{a}>{b},{a>b}')
print(f'{a}=={b},{a==b}')
print(f'{a}!=={b},{a!=b}')

print(f'{a}>={b},{a>b}')
print(f'{a}<={b},{a<b}')

print(f'{a}>{b}and{b}<{a},{a>b and b<a}')#and 都真才为真
print(f'{a}=={b} or {a}>{b},{a==b or a>b}')#or 有真就为真
print(f'not {a}<{b},{not a<b}')#not 逻辑非 取反
print(f'{a}>{b} or {a}<{b},{a>b or b>a}')#逻辑或 有一个为True整个为True

#
# # a = input('请输入')
# # b = input('请输入运算符')
# # c = input('请输入')
# # a_1=float(a)
# # b_1=str(b)
# # C_1=float(c)
# # if b == '+':print(f'{a}{b}{c}=:{a_1:+c_1}')


if a > b:
    print('a>b')
else:
    print('a<=b')