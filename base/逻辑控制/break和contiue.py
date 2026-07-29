# num = 1
# while num <= 10:
#     if num == 3:
#         print(f'第{num}本为空白作业，结束批阅')
#         break
#     print(f'老师正在批阅第{num}本作业')
#     num += 1
# print('循环结束')



num = 1
while num <= 10:
    if num == 3:
        print(f'第{num}本有大量错误，跳过本次循环')
        num += 1
        continue
    print(f'批阅第{num}本作业')
    num += 1
