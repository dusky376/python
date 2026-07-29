student_name = input('输入学生姓名')
chinese_str = input("请输入语文成绩")
math_str = input("请输入数学成绩")
english_str = input('请输入英语成绩')
#格式转换
chinese = float(chinese_str)
math = float(math_str)
english = float(english_str)
#计算总分
total = chinese + math + english
#平均分
avg = total / 3
grade = 0
if avg > 90:
    grade = 'A'
if avg > 80:
    grade = 'B'
if avg > 70:
    grade = 'C'
if avg > 60:
    grade = 'D'
elif avg > 50:
    grade = '不及格'
print(f'学生姓名{student_name},语文成绩{chinese:.2f},英语成绩{english:.2f},数学成绩{math:.2f},成绩评级{grade}')