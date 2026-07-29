
# num = 0
# sum = 0
# while num <= 50:
#     num += 1
#     sum = num + sum
# print(sum)


#从一到五十所有的奇数的和

num = 1
sum = 0
while num <= 50:
    if num % 2 != 0:
        # print(num)
        sum = num + sum
    num += 1
print(f'从一到五十所有奇数的和',{sum})