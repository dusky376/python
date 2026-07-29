'''
小数float
整数int
(',")字符串
列表list 有序可变集合 nums = [1,2,3]

元组tuple 有序不可变集合 info = ["张三"，20]
                              key:value,   key:value
字典dict 键值对集合 student = {"name":"李四"，"age":19}

集合set 无序,不重复序列  num_set={1,3,5}
'''

name='zack'

age=20

weight=60
num = 1
score = 95.5

print(name,age,weight)

'''格式化输出
通过字符串拼接变量值的方式，进行输出，就叫格式化输出，方式f-string
print(f'字符串{变量名})'''
#基础用法
print(f"姓名：{name},年龄：{age},分数：{score}")

#对小数进行控制，保留两位小数
#分数：{score:.2f}（保留两位小数
print(f"姓名：{name},年龄：{age},分数：{score:.2f}")

#对整数进行补0，控制整数位数
#学号：{num:06d}数字补零（6位宽度）
print(f"姓名：{name},学号：{num:06d}，年龄：{age},分数：{score:.2f}")

'''
format()方法输出
'''
print('姓名:{},年龄:{}'.format(name,age))
#format指定输出位置
print('姓名:{0},年龄:{1}'.format(age,name))
#format控制小数位数：.2f
print('成绩{:.2f}'.format(score))

'''
%占位符
'''
print('姓名：%s,年龄：%d,分数:%.2f' % (name,age,score))

'''转义字符
\n换行
\t 表示tab制表符，表示四空格
\转义
" 表示字符串，不能被其他双引号包裹
' 表示字符串，不能被其他双引号包裹
'''
print('hello，我是jack\n我爱编程')
print('hello，i\'m zack')
print("hello，i'm zack")

'''
数字补零d
'''
'''输入函数input()
'''


'''
命名规则：
仅能包含字母数字下划线
不能以数字开头
严格区分大小写
不能使用关键字
'''


'''
判断变量类型：
1.type（变量名），返回变量对应具体类型
2.isinstance（变量名，类型），判断变量名是否和类型匹配，如果匹配返回True，否则返回False

'''
print(type(name))
print(isinstance(age,int))
print(isinstance(weight,float))
