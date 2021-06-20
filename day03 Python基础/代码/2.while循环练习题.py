# 1. 补充代码实现
#    猜数字，设定一个理想数字比如：66，一直提示让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有输入等于66，显示猜测结果正确，然后退出循环。
#      number = 66
#      flag = True
#      while flag:
#      	...

# num = 66
# flag = True
# print("开始")
# while flag:
#     guess_num = int(input("请输入数字:"))
#     if guess_num > num:
#         print("猜大了")
#     elif guess_num < num:
#         print("猜小了")
#     else:
#         print("猜测正确")
#         flag = False
# print("结束")
#
# 2. 使用循环输出1~100所有整数。
# num = 1
# print("开始")
# while num < 101:
#     print(num)
#     num = num + 1
# print("结束")

# num = 1
# print("开始")
# while num:
#     if num < 101:
#         print(num)
#         num = num+1
#     else:
#         num = False
#         print("over")
# print("结束")


# 3. 使用循环输出 1 2 3 4 5 6   8 9 10，即：10以内除7以外的整数。 !!!!!不会写

# num = 1
# print("开始")
# while num < 11:
#     if num == 7:
#         pass
#     else:
#         print(num)
#     num = num + 1 #和if缩进一样

# num = 1
# print("开始")
# while num < 11:
#     if num != 7:
#         print(num)
#     num = num + 1 #和if缩进一样

# 4. 输出 1~100 内的所有奇数。不会
# num = 1
# print("开始")
# while num < 101:
#     if num%2 == 1:
#         print(num)
#     num = num+1
# print("结束")

# 5. 输出 1~100 内的所有偶数。
# num = 1
# print("开始")
# while num < 101:
#     if num%2 == 0:
#         print(num)
#     num = num+1
# print("结束")

# 6. 求 1~100 的所有整数的和。
# total = 0 #0+1/0+1+2/0+1+2+3
# num = 1
# print("开始")
# while num < 101:
#     total = total + num
#     num = num+1
# print(total)
# print("结束")

# 7. 输出10 ~ 1 所有整数。
# num = 10
# while num > 0:
#     print(num)
#     num = num - 1

#思考题 求100以内整数这样的结果:1-2+3-4+5-6...=?
total = 0
num = 1
print("开始")
while num < 101:
    if num%2 == 1:
        total = total + num
    else:
        total = total - num
    num = num+1
print(total)
print("结束")