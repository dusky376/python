'''
同一个变量可以存储不同数据
以最新赋值为值
'''

# age = 100
# print(type(age))
# age = 3.14
# print(type(age))
#
# age = 'hello world'
# print(type(age))
# '''1.age本身不具备类型
# 2。type（age）实际上获取的是age指向的地址单元里存储的数据类型
# 3.age=3为了简化描述，我们就说age类型为整形
# 4.age=3本质上是age存储了3的地址，为了简化描述，我们就说age存储了3
# '''
# #程序从上到下执行，最后age的值是最新赋值地址
# print(f'age:{age}')



'''
eval(x)---->执行x字符串的表达式，将x转化为对应的类型
'''


# product_name = input('请输入商品名称：')
# price_str = input('请输入商品单价：')
# count_str = input('请输入商品数量：')
# #类型转换
# price = float(price_str)
# count = int(count_str)
# total = price * count
# print(f'商品名称{product_name}，商品单价{price:.2f}，商品数量{count}，总价为{total:.2f}')

'''
1。字符串没办法和数值类型的数据惊醒加减除运算
2.字符串和数值做乘法运算，不是做计算，而是将字符串赋值n份凭借起来


'''
name = 'zack'
age = 20
print(f'{name * age}')