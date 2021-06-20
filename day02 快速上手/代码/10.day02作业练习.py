# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
# number = 66
# guess_number = input("请输入数字:")
# if int(guess_number) > number:
#     print("猜大了")
# elif int(guess_number) < number:
#     print("猜小了")
# else:
#     print("结果正确")

# 提示⽤户输入 "爸爸" ，判断⽤户输入的对不对。如果对, 提示真聪明, 如果不对, 提示你是傻逼么。
# content = input("请输入内容:")
# if content == "爸爸":
#     print("真聪明")
# else:
#     print("你是傻逼么")

# 写程序，成绩有ABCDE5个等级，与分数的对应关系如下.
# A    90-100
# B    80-89
# C    60-79
# D    40-59
# E    0-39
# 要求用户输入0-100的数字后，你能正确打印他的对应成绩等级.

score = int(input("请输入你的成绩:"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 60 <= score <= 79:
    print("C")
elif 40 <= score <= 59:
    print("D")
elif 0 <= score <= 39:
    print("E")
else:
    print("输入有误")

# 另外一种答案
# score = input("请输入分数")
# data = int(score)
#
# if data >= 90 and data <= 100:
#   print("A")
# elif data >= 80 and data <90:
#   print("B")
# elif data >= 60 and data <80:
#   print("C")
# elif data >= 40 and data <60:
#   print("D")
# elif data >= 0 and data <40:
#   print("E")
# else:
#   print("输入错误")