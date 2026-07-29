'''
if 条件表达式：
    满足条件时执行的代码块（缩进）
age=19
if age >= 18:
    print('你已成年，可独立出行')
else:
    print('你未成年，需由监护人陪同')
'''


#
# a_1 = float(input('请输入'))
# b_1 = str(input('请输入运算符'))
# c_1 = float(input('请输入'))
# if b_1 == '+':
#     d = a_1 + c_1
#     print(f'{a_1} + {c_1}={d:.5f},')
# elif b_1 == '-':
#     d = a_1 - c_1
#     print(f'{a_1} - {c_1}={d:.5f}')
# elif b_1 == '*':
#     d = a_1 * c_1
#     print(f'{a_1} * {c_1}={d:.5f}')
# elif b_1 == '/':
#     d = a_1 / c_1
#     print(f'{a_1} / {c_1}={d:.5f}')
# elif b_1 == '%':
#     d = a_1 % c_1
#     print(f'{a_1} % {c_1}={d:.5f}')
# elif b_1 == '//':
#     d = a_1 // c_1
#     print(f'{a_1} // {c_1}={d:.5f}')
# elif b_1 == '**':
#     d = a_1 ** c_1
#     print(f'{a_1} ** {c_1}={d:.f}')

# age = int(input('请输入年龄'))
# if age >= 18:
#     print('你已成年可以观看电影')
# elif age < 18:
#     print('你需要在家长的陪同下观看电影')


# score = float(input('请输入成绩'))
# if score >= 90:
#     print('你的成绩优秀')
# elif score >= 80:
#     print('你的成绩良好')
# elif score >= 70:
#     print('你的成绩中等')
# elif score >= 60:
#     print('你的成绩及格')
# else:
#     print('你的成绩不合格')




'''多重嵌套'''
# age = int(input('请输入年龄'))
# if age >= 18:
#     print('你的年龄符合要求')
#     height = float(input('请输入你的身高'))
#     if height >= 150:
#         print('符合要求,可以报名')
#     else :
#         print('不符合申报条件')
# else :
#     print('你还未成年，不允许申报')



'''条件表达式的高级用法'''
# hour = int(input('请输入工作时间（0-23）：'))
# weekday = str(input('是否是工作日：'))
# if (weekday == '是'or '对') and 0 <= hour <= 23:
#     print('现在是工作时间，请好好工作')
# else:
#     print('好好休息')



'''三元表达式'''
age = 20
# if age >= 18:
#     result = '成年'
# else:
#     result = '未成年'
#
result = '成年' if age >= 18 else '未成年'
print(result)