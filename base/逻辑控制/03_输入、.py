'''输入函数input
变量 = input(字符串)
变量存储用户输入的信息
input是一个阻塞型函数
字符串是可选的，用来提示用户输入的内容
'''


#这样无法显示内容提示用户输入
#name = input()
#提示用户输入姓名
#name = input('请输入用户姓名：')
#提示用户输入密码
#pwd = input('请输入密码')
#print(f'用户姓名为：{name},密码为：{pwd}')

#age = input('请输入年龄：')
#print(f'age的类型：{type(age)}')



#请输入商品单价
price = input('请输入商品单价')
#将price由字符串转化为整数
price_n=int(price)

#请输入商品数量
count = input('请输入商品数量')
count_n=int(count)

#计算总价
total_price = price_n * count_n
print(f'总价为{total_price}')